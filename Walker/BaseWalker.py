from picotool.pico8.lua.parser import *


def walk_stat_assignment(node):
    # for now
    exps = node.explist.exps
    vars = node.varlist.vars
    assert (len(vars) == len(exps))
    for exp, var in zip(exps, vars):
        return walk_var_name(var) + " = " + walk_exp(exp)
    print(node)


def walk_table_constructor(node):
    list_half = []
    dict_half = {}
    for field in node.fields:
        match type(field).__name__:
            case "FieldExp":
                list_half.append(walk_exp_value(field.exp))
            case "FieldNamedKey":
                dict_half[walk_tok_name(field.key_name)] = walk_exp_value(field.exp)
            case _:
                raise NotImplementedError("Not implemented yet")
    list_half = f'[{",".join(list_half)}]'
    dict_half = "{"+",".join([f"{i}={j}" for i,j in dict_half.items()])+"}"
    return 'Table(' + list_half + ',' + dict_half + ')'

def walk_tok_name(node):
    return str(node.value)


def walk_exp_value(node):
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
            return walk_table_constructor(node.value)
        case "VarName":
            return walk_var_name(node.value)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_exp(node):
    match type(node).__name__:
        case "ExpValue":
            return walk_exp_value(node)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk_var_name(node):
    assert (type(node).__name__ == "VarName")
    return node.name.value.decode("utf-8")


def walk_chunk(node):
    lines = []
    for statement in node.stats:
        lines.append(walk_statement(statement))
    return "\n".join(lines)


def walk_statement(node):
    match type(node).__name__:
        case "StatAssignment":
            return walk_stat_assignment(node)
        case _:
            raise NotImplementedError("Not implemented yet")


def walk(node):
    match type(node).__name__:
        case "Chunk":
            return walk_chunk(node)
        case "StatAssignment":
            return walk_stat_assignment(node)
        case _:
            raise NotImplementedError("Not implemented yet")
