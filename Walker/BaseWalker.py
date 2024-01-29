from picotool.pico8.lua.parser import *


def walk_stat_assignment(node, depth):
    # for now
    exps = node.explist.exps
    vars = node.varlist.vars
    vars_as_code = []
    exps_as_code = []
    assert (len(vars) == len(exps))
    for exp, var in zip(exps, vars):
        vars_as_code.append(walk_var_name(var))
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
                dict_half[walk_tok_name(field.key_name)] = walk_exp(field.exp, depth)
            case _:
                raise NotImplementedError("Not implemented yet")
    list_half = f'[{",".join(list_half)}]'
    dict_half = "{" + ",".join([f"{i}={j}" for i, j in dict_half.items()]) + "}"
    return 'Table(' + list_half + ',' + dict_half + ')'


def walk_tok_name(node):
    return str(node.value)


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
        case "ExpBinOp":
            return walk_exp(node.value, depth)
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
    op, spaces = get_bin_op(node.binop)
    exp1 = walk_exp(node.exp1, depth)
    exp2 = walk_exp(node.exp2, depth)
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
        return "!=", 0
    elif value == "^^":
        return "^", 0
    elif value == "^":
        return "**", 0
    elif value == "\\":
        return "//", 0
    elif value == "..":
        return "+", 0
    elif value == "and" or value == "or":
        return value, 1
    return value, 0


def walk_statement(node, depth=0):
    match type(node).__name__:
        case "StatAssignment":
            return walk_stat_assignment(node, depth)
        case "StatFunctionCall":
            return walk_stat_function_call(node,depth)
        case "StatIf":
            return walk_stat_if(node, depth)
        # case "StatFunction":
        #     return walk_stat_function(node,depth)
        case _:
            raise NotImplementedError("Not implemented yet")


# def walk_stat_function(node, depth):
#     chunk = walk_chunk(node.funcbody)


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
    function_name = walk_var_name(node.functioncall.exp_prefix)
    args = walk_function_call_args(node.functioncall.args, depth)
    return f"{function_name}{args}"


def walk_function_call_args(node, depth):
    match type(node).__name__:
        case "TokString":
            return f"({str(node.value)})"
        case "FunctionArgs":
            args = []
            for exp in node.explist.exps:
                args.append(walk_exp(exp, depth))
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
