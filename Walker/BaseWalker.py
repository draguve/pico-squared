from picotool.pico8.lua.parser import *


def walk_stat_assignment(node, depth):
    # for now
    exps = node.explist.exps
    vars = node.varlist.vars
    vars_as_code = []
    exps_as_code = []
    assert (len(vars) == len(exps))
    for exp, var in zip(exps, vars):
        vars_as_code.append(walk_var(var, depth))
        exps_as_code.append(walk_exp(exp, depth))
    return ",".join(vars_as_code) + " = " + ",".join(exps_as_code)


def walk_table_constructor(node, depth):
    list_half = []
    dict_half = {}
    for field in node.fields:
        match type(field).__name__:
            case "FieldExp":
                list_half.append(walk_exp(field.exp, depth))
            case "FieldNamedKey":
                dict_half[f"b'{walk_tok_name(field.key_name, depth)}'"] = walk_exp(field.exp, depth)
            case "FieldExpKey":
                dict_half[walk_exp(field.key_exp, depth)] = walk_exp(field.exp, depth)
            case _:
                raise NotImplementedError("Not implemented yet")
    list_half = f'[{",".join(list_half)}]'
    dict_half = "{" + ",".join([f"{i}:{j}" for i, j in dict_half.items()]) + "}"
    return 'Table(' + list_half + ',' + dict_half + ')'


def walk_tok_name(node, depth):
    assert (type(node).__name__ == "TokName")
    return node.value.decode("utf-8")


def walk_exp_value(node, depth):
    match type(node.value).__name__:
        case "TokNumber":
            return str(node.value.value)
        case "TokString":
            return str(node.value.value)
        case "bool":
            return str(node.value)
        case "NoneType":
            return str(node.value)
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
        # case "Function":
        #     return walk_function_body(node.funcbody, depth)
        case _:
            raise NotImplementedError("Not implemented yet")


# def walk_function_body(node, depth):
#     pass


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
    return f"{prefix}[{index_exp}]"


def walk_var_attribute(node, depth):
    assert (type(node).__name__ == "VarAttribute")
    prefix = walk_var(node.exp_prefix, depth)
    attr_name = walk_tok_name(node.attr_name, depth)
    return f"{prefix}[b'{attr_name}']"


def walk_var_name(node):
    assert (type(node).__name__ == "VarName")
    return node.name.value.decode("utf-8")


def walk_chunk(node, depth=0):
    lines = []
    for statement in node.stats:
        lines.append(walk_statement(statement, depth=depth))
    if len(lines) == 0:
        lines.append("pass")
    lines = [f"{'    ' * depth}{line}" for line in lines]
    return "\n".join(lines)


def walk_exp_un_op(node, depth):
    op, spaces, is_func = get_un_op(node.unop)
    exp = walk_exp(node.exp, depth)
    if is_func:
        return f"{op}({exp})"
    return f"{op}{' ' * spaces}{exp}"


def walk_exp_bin_op(node, depth):
    op, spaces, is_func = get_bin_op(node.binop)
    exp1 = walk_exp(node.exp1, depth)
    exp2 = walk_exp(node.exp2, depth)
    if is_func:
        return f"{op}({exp1},{exp2})"
    return f"({exp1}{' ' * spaces}{op}{' ' * spaces}{exp2})"
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
    if value == "~=":
        return "!=", 0, False
    elif value == "^^":
        return "^", 0, False
    elif value == "^":
        return "**", 0, False
    elif value == "\\":
        return "//", 0, False
    elif value == "..":
        return "PicoStrConcat", 0, True
    elif value == "and" or value == "or":
        return value, 1, False
    return value, 0, False


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


def walk_stat_local_assignment(node, depth):
    # for now
    exps = [walk_exp(exp, depth) for exp in node.explist.exps]
    names = [walk_tok_name(name, depth) for name in node.namelist.names]
    assert (len(exps) == len(names))
    return ",".join(names) + " = " + ",".join(exps)


def walk_stat_return(node, depth):
    return_val = []
    if node.explist is not None:
        return_val = [walk_exp(exp, depth) for exp in node.explist.exps]
    return f"return {','.join(return_val)}".strip()


def walk_stat_function(node, depth):
    func_body = walk_func_body(node.funcbody, depth)
    name_path = [walk_tok_name(name, depth) for name in node.funcname.namepath]
    return f"def {'.'.join(name_path)}{func_body}\n"


def walk_func_body(node, depth):
    code = walk_chunk(node.block, depth + 1)
    parameter_list = []
    if node.parlist is not None:
        parameter_list = [walk_tok_name(name, depth) for name in node.parlist.names]
    return f"({','.join(parameter_list)}):\n{code}"


def walk_stat_break(node, depth):
    assert type(node).__name__ == "StatBreak"
    return "break"


def walk_stat_repeat(node, depth):
    code_chunk = walk_chunk(node.block, depth)
    # TODO make this better MAYBE ( not required)
    code_chunk_inside = walk_chunk(node.block, depth + 1)
    condition = walk_exp(node.exp, depth)
    code_inside = walk_chunk(node.block, depth + 1)
    if code_chunk.strip() == "pass":
        return f"while {condition}:\n{code_inside}"
    return f"{code_chunk}\nwhile {condition}:\n{code_chunk_inside}"


def walk_for_in_iter(function_call, depth):
    args = walk_function_call_args(function_call.args, depth)
    function_name = walk_var(function_call.exp_prefix)
    match function_name:
        case "pairs":
            assert len(function_call.args.explist.exps) == 1
            return f"ipairs{args}"
        case "all":
            assert len(function_call.args.explist.exps) == 1
            return f"iall{args}"
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_stat_for_in(node, depth):
    code_inside = walk_chunk(node.block, depth + 1)
    name_list = [walk_tok_name(name, depth) for name in node.namelist.names]
    assert len(node.explist.exps) == 1
    iter_call = walk_for_in_iter(node.explist.exps[0].value, depth)
    return f"for {','.join(name_list)} in {iter_call}:\n{code_inside}"


def walk_stat_for_step(node, depth):
    code_inside = walk_chunk(node.block, depth + 1)
    # Todo fix this +1
    range_args = [walk_exp(node.exp_init, depth), walk_exp(node.exp_end, depth)]
    variable_name = walk_tok_name(node.name, depth)
    if node.exp_step is not None:
        range_args.append(walk_exp(node.exp_step, depth))
    return f"for {variable_name} in pico_range({','.join(range_args)}):\n{code_inside}"


def walk_stat_while(node, depth):
    condition = walk_exp(node.exp, depth)
    code_inside = walk_chunk(node.block, depth + 1)
    return f"while {condition}:\n{code_inside}"


def walk_stat_if(node, depth):
    conditions = []
    code = []
    first = True
    final = ""
    for cond, chunk in node.exp_block_pairs:
        chunk_out = walk_chunk(chunk, depth + 1)

        condition = None
        if cond is not None:
            condition = walk_exp(cond, depth)
        if first:
            assert condition is not None
            final += f"if {condition}:\n{chunk_out}\n"
            first = False
            continue
        elif condition is None:
            final += f"else:\n{chunk_out}\n"
        else:
            final += f"elif {condition}:\n{chunk_out}\n"
    return final


def walk_stat_function_call(node, depth):
    return walk_function_call(node.functioncall, depth)


def walk_function_call(node, depth):
    function_name = walk_var_name(node.exp_prefix)
    args = walk_function_call_args(node.args, depth)
    return f"{function_name}{args}"


def walk_function_call_args(node, depth):
    match type(node).__name__:
        case "TokString":
            return f"({str(node.value)})"
        case "FunctionArgs":
            args = []
            if node.explist is not None:
                args = [walk_exp(exp, depth) for exp in node.explist.exps]
            return f"({','.join(args)})"
        case "TableConstructor":
            return f"({walk_table_constructor(node, depth)})"
        case _:
            raise NotImplementedError("Not implemented yet")


def walk(node, depth):
    match type(node).__name__:
        case "Chunk":
            return walk_chunk(node)
        case "StatAssignment":
            return walk_stat_assignment(node, depth)
        case _:
            raise NotImplementedError("Not implemented yet")
