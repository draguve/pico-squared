from picotool.pico8.lua.parser import *
from dataclasses import dataclass, InitVar, field
from Util import get_random_string, clamp


@dataclass
class ParserReturn:
    line: str
    prev_lines: list[str] = field(default_factory=list)
    variables: set = field(default_factory=set)
    function_defs: set = field(default_factory=set)
    function_calls: set = field(default_factory=set)
    locals: set = field(default_factory=set)
    old: InitVar[object | None] = None

    def __post_init__(self, old):
        if old is not None:
            old.prev_lines.extend(self.prev_lines)
            self.prev_lines = old.prev_lines
            self.variables = old.variables.union(self.variables)
            self.function_defs = old.function_defs.union(self.function_defs)
            self.function_calls = old.function_calls.union(self.function_calls)
            self.locals = old.locals.union(self.locals)


def combine_rest(*returns):
    prev_lines = []
    prev_variables = set()
    prev_funcs = set()
    prev_calls = set()
    prev_locals = set()
    for arg in returns:
        prev_lines.extend(arg.prev_lines)
        prev_variables = prev_variables.union(arg.variables)
        prev_funcs = prev_funcs.union(arg.function_defs)
        prev_calls = prev_calls.union(arg.function_calls)
        prev_locals = prev_locals.union(arg.locals)
    return ParserReturn("", prev_lines=prev_lines, variables=prev_variables, function_defs=prev_funcs,
                        function_calls=prev_calls, locals=prev_locals)


def parser_return_lines(arr: list[ParserReturn]):
    return [i.line for i in arr]


def get_all_set_variables(arr: list[ParserReturn]):
    to_return = set()
    for parser in arr:
        to_return = to_return.union(parser.variables)
    return to_return


def walk(node, depth):
    match type(node).__name__:
        case "Chunk":
            chunk = walk_chunk(node, declare_globals=False, is_global=True)
            assert len(chunk.prev_lines) == 0
            return chunk.line
        # case "StatAssignment":
        #     return walk_stat_assignment(node, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_statement(node, depth=0):
    match type(node).__name__:
        case "StatAssignment":
            return walk_stat_assignment(node, depth)
        case "StatFunctionCall":
            return walk_stat_function_call(node, depth)
        case "StatIf":
            return walk_stat_if(node, depth)
        case "StatFunction":
            return walk_stat_function(node, depth)
        case "StatWhile":
            return walk_stat_while(node, depth)
        case "StatForStep":
            return walk_stat_for_step(node, depth)
        case "StatForIn":
            return walk_stat_for_in(node, depth)
        case "StatRepeat":
            return walk_stat_repeat(node, depth)
        case "StatBreak":
            return walk_stat_break(node, depth)
        case "StatReturn":
            return walk_stat_return(node, depth)
        case "StatLocalAssignment":
            return walk_stat_local_assignment(node, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_stat_assignment(node, depth):
    vars = [walk_var(var, depth) for var in node.varlist.vars]
    exps = [walk_exp(exp, depth) for exp in node.explist.exps]
    assert (len(vars) == len(exps))
    assignop = node.assignop.value.decode("utf-8")
    if assignop == "=":
        return ParserReturn(",".join([var.line for var in vars]) + " = " + ",".join([exp.line for exp in exps]),
                            old=combine_rest(*vars, *exps))
    else:
        assert (len(vars) == 1)
        exp1, exp2 = vars[0], exps[0]
        op, spaces, is_func = _get_bin_op(assignop.replace("=", ""))
        if is_func:
            return ParserReturn(f"{exp1.line} = {op}({exp1.line},{exp2.line})", old=combine_rest(exp1, exp2))
        return ParserReturn(f"{exp1.line} = ({exp1.line}{' ' * spaces}{op}{' ' * spaces}{exp2.line})",
                            old=combine_rest(exp1, exp2))


def walk_table_constructor(node, depth):
    list_half = []
    dict_half = {}
    old = ParserReturn("")
    for node_field in node.fields:
        match type(node_field).__name__:
            case "FieldExp":
                exp = walk_exp(node_field.exp, depth)
                old = combine_rest(old, exp)
                list_half.append(exp.line)
            case "FieldNamedKey":
                name = walk_tok_name(node_field.key_name, depth)
                exp = walk_exp(node_field.exp, depth)
                old = combine_rest(old, name, exp)
                dict_half[f"b'{name.line}'"] = exp.line
            case "FieldExpKey":
                key_exp = walk_exp(node_field.key_exp, depth)
                value_exp = walk_exp(node_field.exp, depth)
                old = combine_rest(old, key_exp, value_exp)
                dict_half[key_exp.line] = value_exp.line
            case _:
                raise NotImplementedError("Not implemented yet")
    list_half = f'[{",".join(list_half)}]'
    dict_half = "{" + ",".join([f"{i}:{j}" for i, j in dict_half.items()]) + "}"
    return ParserReturn('Table(' + list_half + ',' + dict_half + ')', old=old)


def walk_tok_name(node, depth):
    assert (type(node).__name__ == "TokName")
    return ParserReturn(str(node.value)[2:-1])


def walk_exp_value(node, depth):
    match type(node.value).__name__:
        case "TokNumber":
            return ParserReturn(str(node.value.value))
        case "TokString":
            return ParserReturn(str(node.value.value))
        case "bool":
            return ParserReturn(str(node.value))
        case "NoneType":
            return ParserReturn(str(node.value))
        case "TableConstructor":
            return walk_table_constructor(node.value, depth)
        case "VarName":
            return walk_var_name(node.value)
        case "VarAttribute":
            return walk_var_attribute(node.value, depth)
        case "VarIndex":
            return walk_var_index(node.value, depth)
        case "ExpBinOp":
            return walk_exp(node.value, depth)
        case "FunctionCall":
            return walk_function_call(node.value, depth)
        case "Function":
            return walk_function(node.value, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


# when passed as value
def walk_function(node, depth):
    func_name = f"anon_{get_random_string(10)}"
    func_body = walk_func_body(node.funcbody, depth)
    return ParserReturn(func_name, [f"def {func_name}{func_body.line}"], function_defs={func_name, })


def walk_exp(node, depth):
    match type(node).__name__:
        case "ExpValue":
            return walk_exp_value(node, depth)
        case "ExpBinOp":
            return walk_exp_bin_op(node, depth)
        case "ExpUnOp":
            return walk_exp_un_op(node, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_var(node, depth):
    match type(node).__name__:
        case "VarName":
            return walk_var_name(node)
        case "VarAttribute":
            return walk_var_attribute(node, depth)
        case "VarIndex":
            return walk_var_index(node, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_var_index(node, depth):
    prefix = walk_var(node.exp_prefix, depth)
    index_exp = walk_exp(node.exp_index, depth)
    return ParserReturn(f"{prefix.line}[{index_exp.line}]", old=combine_rest(prefix, index_exp))


def walk_var_attribute(node, depth):
    assert (type(node).__name__ == "VarAttribute")
    prefix = walk_var(node.exp_prefix, depth)
    attr_name = walk_tok_name(node.attr_name, depth)
    return ParserReturn(f"{prefix.line}[b'{attr_name.line}']", old=combine_rest(prefix, attr_name))


def walk_var_name(node):
    assert (type(node).__name__ == "VarName")
    variableName = node.name.value.decode("utf-8")
    return ParserReturn(variableName, variables={variableName, })


def walk_chunk(node, depth=0, declare_globals=True, params=None, is_global=False, varargs=False):
    lines = []
    if params is None:
        params = set()
    if varargs:
        name = f"vararg_{get_random_string(10)}"
        lines.append(ParserReturn(name + ' = Table(argv,{b"#":len('+name+')})'))
    statements = [walk_statement(statement, depth=depth) for statement in node.stats]
    for statement in statements:
        if statement.prev_lines is not None:
            for prev_line in statement.prev_lines:
                lines.extend([ParserReturn(stat) for stat in prev_line.split('\n')])
            statement.prev_lines = []
        lines.extend([ParserReturn(stat) for stat in statement.line.split('\n')])
    if len(lines) == 0:
        lines.append(ParserReturn("pass"))
    old = combine_rest(*statements)
    if declare_globals:
        used_globals = old.variables.difference(params).difference(old.locals)
        if varargs:
            used_globals.discard("arg")
        if len(used_globals) > 0:
            lines.insert(0, ParserReturn(f"global {','.join(list(used_globals))}"))
        old.variables = used_globals
    if is_global:
        if len(old.variables) > 0:
            lines.insert(0, ParserReturn(
                f"{','.join(list(old.variables))} = {','.join([str(None) for _ in range(len(old.variables))])}"))
    lines_text = [f"{'    ' * clamp(depth, 0, 1)}{line.line}" for line in lines]
    return ParserReturn("\n".join(lines_text), old=old)


def walk_exp_un_op(node, depth):
    op, spaces, is_func = get_un_op(node.unop)
    exp = walk_exp(node.exp, depth)
    if is_func:
        return ParserReturn(f"{op}({exp.line})", old=exp)
    return ParserReturn(f"{op}{' ' * spaces}{exp.line}", old=exp)


def walk_exp_bin_op(node, depth):
    op, spaces, is_func = get_bin_op(node.binop)
    exp1 = walk_exp(node.exp1, depth)
    exp2 = walk_exp(node.exp2, depth)
    if is_func:
        return ParserReturn(f"{op}({exp1.line},{exp2.line})", old=combine_rest(exp1, exp2))
    return ParserReturn(f"({exp1.line}{' ' * spaces}{op}{' ' * spaces}{exp2.line})", old=combine_rest(exp1, exp2))
    # raise NotImplementedError("Not implemented yet")


def get_un_op(value):
    value = value.value.decode("utf-8")
    if value == 'not':
        return value, 1, False
    if value == "#":
        return "len", 0, True
    return value, 0, False


def get_bin_op(value):
    value = value.value.decode("utf-8")
    return _get_bin_op(value)


def _get_bin_op(value):
    match value:
        case "~=":
            return "!=", 0, False
        case "^^":
            return "^", 0, False
        case "^":
            return "**", 0, False
        case "\\":
            return "//", 0, False
        case "..":
            return "PicoStrConcat", 0, True
        case "and":
            return value, 1, False
        case "or":
            return value, 1, False
        case ">>>":
            return "PicoNumber.lsr", 0, True
        case "<<>":
            return "PicoNumber.rotl", 0, True
        case ">><":
            return "PicoNumber.rotr", 0, True
        case _:
            return value, 0, False


def walk_stat_local_assignment(node, depth):
    # for now
    names = [walk_tok_name(name, depth) for name in node.namelist.names]
    if node.explist is not None:
        exps = [walk_exp(exp, depth) for exp in node.explist.exps]
    else:
        exps = [ParserReturn(str(None)) for _ in range(len(names))]
    assert (len(exps) == len(names))
    return ParserReturn(",".join(parser_return_lines(names)) + " = " + ",".join(parser_return_lines(exps)),
                        old=combine_rest(*exps, *names), locals=set(parser_return_lines(names)))


def walk_stat_return(node, depth):
    return_val = []
    if node.explist is not None:
        return_val = [walk_exp(exp, depth) for exp in node.explist.exps]
    return ParserReturn(f"return {','.join(parser_return_lines(return_val))}".strip(), old=combine_rest(*return_val))


def walk_stat_function(node, depth):
    func_body = walk_func_body(node.funcbody, depth)
    name_path = [walk_tok_name(name, depth) for name in node.funcname.namepath]
    function_name = '.'.join(parser_return_lines(name_path))
    return ParserReturn(f"def {function_name}{func_body.line}", old=combine_rest(*name_path, func_body),
                        function_defs={function_name, })


def walk_func_body(node, depth):
    parameter_list = []
    varargs = False
    if node.parlist is not None:
        parameter_list = [walk_tok_name(name, depth) for name in node.parlist.names]
    params = set(parser_return_lines(parameter_list))
    if node.dots is not None:
        parameter_list.append(ParserReturn("*argv"))
        varargs = True
    code = walk_chunk(node.block, depth + 1, True, params,varargs=varargs)
    return ParserReturn(f"({','.join(parser_return_lines(parameter_list))}):\n{code.line}",
                        old=combine_rest(*parameter_list, code))


def walk_stat_break(node, depth):
    assert type(node).__name__ == "StatBreak"
    return ParserReturn("break")


def walk_stat_repeat(node, depth):
    code_chunk = walk_chunk(node.block, depth, False)
    # TODO make this better MAYBE ( not required)
    code_chunk_inside = walk_chunk(node.block, depth + 1, False)
    condition = walk_exp(node.exp, depth)
    code_inside = walk_chunk(node.block, depth + 1, False)
    if code_chunk.line.strip() == "pass":
        return ParserReturn(f"while {condition.line}:\n{code_inside.line}", old=combine_rest(condition, code_inside))
    return ParserReturn(f"{code_chunk.line}\nwhile {condition.line}:\n{code_chunk_inside.line}",
                        old=combine_rest(code_chunk, condition))


def walk_for_in_iter(function_call, depth):
    args = walk_function_call_args(function_call.args, depth)
    function_name = walk_var(function_call.exp_prefix, depth)
    match function_name.line:
        case "pairs":
            assert len(function_call.args.explist.exps) == 1
            return ParserReturn(f"ipairs{args.line}", old=combine_rest(args, function_name))
        case "all":
            assert len(function_call.args.explist.exps) == 1
            return ParserReturn(f"iall{args.line}", old=combine_rest(args, function_name))
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_stat_for_in(node, depth):
    code_inside = walk_chunk(node.block, depth + 1, False)
    name_list = [walk_tok_name(name, depth) for name in node.namelist.names]
    assert len(node.explist.exps) == 1
    iter_call = walk_for_in_iter(node.explist.exps[0].value, depth)
    return ParserReturn(f"for {','.join(parser_return_lines(name_list))} in {iter_call.line}:\n{code_inside.line}",
                        old=combine_rest(code_inside, *name_list, iter_call))


def walk_stat_for_step(node, depth):
    code_inside = walk_chunk(node.block, depth + 1, False)
    # Todo fix this +1
    range_args = [walk_exp(node.exp_init, depth), walk_exp(node.exp_end, depth)]
    variable_name = walk_tok_name(node.name, depth)
    if node.exp_step is not None:
        range_args.append(walk_exp(node.exp_step, depth))
    return ParserReturn(
        f"for {variable_name.line} in pico_range({','.join(parser_return_lines(range_args))}):\n{code_inside.line}",
        old=combine_rest(variable_name, *range_args, code_inside))


def walk_stat_while(node, depth):
    condition = walk_exp(node.exp, depth)
    code_inside = walk_chunk(node.block, depth + 1, False)
    return ParserReturn(f"while {condition.line}:\n{code_inside.line}", old=combine_rest(condition, code_inside))


def walk_stat_if(node, depth):
    conditions = []
    code = []
    first = True
    final = ""
    old = ParserReturn("")
    for cond, chunk in node.exp_block_pairs:
        chunk_out = walk_chunk(chunk, depth + 1, False)
        condition = None
        if cond is not None:
            condition = walk_exp(cond, depth)
        if first:
            assert condition is not None
            final += f"if {condition.line}:\n{chunk_out.line}"
            old = combine_rest(old, condition, chunk_out)
            first = False
            continue
        elif condition is None:
            final += f"\nelse:\n{chunk_out.line}"
            old = combine_rest(old, chunk_out)
        else:
            final += f"\nelif {condition.line}:\n{chunk_out.line}"
            old = combine_rest(old, condition, chunk_out)
    return ParserReturn(final, old=old)


def walk_stat_function_call(node, depth):
    return walk_function_call(node.functioncall, depth)


def walk_function_call(node, depth):
    function_name = walk_var_name(node.exp_prefix)  # TODO This would need to be changed later prob

    # move the variables to function calls as its only gonna have the name of the function
    function_name.function_calls = function_name.variables
    function_name.variables = set()

    args = walk_function_call_args(node.args, depth)
    return ParserReturn(f"{function_name.line}{args.line}", old=combine_rest(function_name, args))


def walk_function_call_args(node, depth):
    match type(node).__name__:
        case "TokString":
            return ParserReturn(f"({str(node.value)})")
        case "FunctionArgs":
            args = []
            if node.explist is not None:
                args = [walk_exp(exp, depth) for exp in node.explist.exps]
            return ParserReturn(f"({','.join(parser_return_lines(args))})", old=combine_rest(*args))
        case "TableConstructor":
            table = walk_table_constructor(node, depth)
            return ParserReturn(f"({table.line})", old=table)
        case _:
            raise NotImplementedError("Not implemented yet")
