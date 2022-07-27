import sys
from antlr4 import *

from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaVisitor import LuaVisitor
from pprint import pprint


def print_decorator(func):
    def inner1(*args, **kwargs):
        # calling the actual function now
        # inside the wrapper function.
        data = func(*args, **kwargs)
        print(data)
        return data

    return inner1


# Not all functions
inbuilt_functions = {

    # Graphics
    "clip": {
        "args": [{"argSize": -1, "type": "Tuple"}]
    },
    "fget": {
        "args": [{"argSize": 1, "type": "Number"}, {"argSize": 2, "type": "Bool"}]
    },
    "pget": {
        "args": [{"argSize": -1, "type": "Number"}, ]
    },
    "print": {
        "args": [{"argSize": -1, "type": "Number"}, ]
    },
    "sget": {
        "args": [{"argSize": -1, "type": "Number"}, ]
    },
    "camera": {"args": [{"argSize": -1, "type": "nil"}]},
    "circ": {"args": [{"argSize": -1, "type": "nil"}]},
    "circfill": {"args": [{"argSize": -1, "type": "nil"}]},
    "oval": {"args": [{"argSize": -1, "type": "nil"}]},
    "ovalfill": {"args": [{"argSize": -1, "type": "nil"}]},
    "cls": {"args": [{"argSize": -1, "type": "nil"}]},
    "color": {"args": [{"argSize": -1, "type": "nil"}]},
    "cursor": {"args": [{"argSize": -1, "type": "nil"}]},
    "sspr": {"args": [{"argSize": -1, "type": "nil"}]},
    "tline": {"args": [{"argSize": -1, "type": "nil"}]},
    "spr": {"args": [{"argSize": -1, "type": "nil"}]},
    "sset": {"args": [{"argSize": -1, "type": "nil"}]},
    "fillp": {"args": [{"argSize": -1, "type": "nil"}]},
    "fset": {"args": [{"argSize": -1, "type": "nil"}]},
    "line": {"args": [{"argSize": -1, "type": "nil"}]},
    "pal": {"args": [{"argSize": -1, "type": "nil"}]},
    "palt": {"args": [{"argSize": -1, "type": "nil"}]},
    "pset": {"args": [{"argSize": -1, "type": "nil"}]},
    "rect": {"args": [{"argSize": -1, "type": "nil"}]},
    "rectfill": {"args": [{"argSize": -1, "type": "nil"}]},

    # Tables
    "all": {"args": [{"argSize": -1, "type": "Iterator"}]},
    "count": {"args": [{"argSize": -1, "type": "Number"}]},
    "ipairs": {"args": [{"argSize": -1, "type": "Iterator"}]},
    "pack": {"args": [{"argSize": -1, "type": "Table-Array"}]},
    "pairs": {"args": [{"argSize": -1, "type": "Iterator"}]},
    "unpack": {"args": [{"argSize": -1, "type": "Tuple"}]},
    "next": {"args": [{"argSize": -1, "type": "Any"}]},
    "add": {"args": [{"argSize": -1, "type": "nil"}]},
    "foreach": {"args": [{"argSize": -1, "type": "nil"}]},

    # Input
    "btn": {"args": [{"argSize": 1, "type": "Bool"}, {"argSize": 0, "type": "Number"}]},
    "btnp": {"args": [{"argSize": 1, "type": "Bool"}, {"argSize": 0, "type": "Number"}]},

    # Music
    "music": {"args": [{"argSize": -1, "type": "nil"}]},
    "sfx": {"args": [{"argSize": -1, "type": "nil"}]},

    # Numbers
    "abs": {"args": [{"argSize": -1, "type": "Number"}]},
    "atan2": {"args": [{"argSize": -1, "type": "Number"}]},
    "band": {"args": [{"argSize": -1, "type": "Number"}]},
    "bnot": {"args": [{"argSize": -1, "type": "Number"}]},
    "bor": {"args": [{"argSize": -1, "type": "Number"}]},
    "bxor": {"args": [{"argSize": -1, "type": "Number"}]},
    "ceil": {"args": [{"argSize": -1, "type": "Number"}]},
    "cos": {"args": [{"argSize": -1, "type": "Number"}]},
    "flr": {"args": [{"argSize": -1, "type": "Number"}]},
    "lshr": {"args": [{"argSize": -1, "type": "Number"}]},
    "max": {"args": [{"argSize": -1, "type": "Number"}]},
    "mid": {"args": [{"argSize": -1, "type": "Number"}]},
    "min": {"args": [{"argSize": -1, "type": "Number"}]},
    "rnd": {"args": [{"argSize": 1, "type": "Number", "argType": "Number"}]},
    "rotl": {"args": [{"argSize": -1, "type": "Number"}]},
    "rotr": {"args": [{"argSize": -1, "type": "Number"}]},
    "sgn": {"args": [{"argSize": -1, "type": "Number"}]},
    "shl": {"args": [{"argSize": -1, "type": "Number"}]},
    "shr": {"args": [{"argSize": -1, "type": "Number"}]},
    "sin": {"args": [{"argSize": -1, "type": "Number"}]},
    "sqrt": {"args": [{"argSize": -1, "type": "Number"}]},
    "srand": {"args": [{"argSize": -1, "type": "Number"}]},

}


#
# special = {
# del(t, v) #return deleted
# deli(t, i)
# }


class LuaTypesListener(LuaVisitor):
    def __init__(self):
        self.current_func = {}
        self.globals = {}
        self.functions = {}

    # What about local functions
    def visitFunctionDeclaration(self, ctx: LuaParser.FunctionDeclarationContext):
        names = []
        name = ctx.funcname().NAME()
        for n in name:
            names.append(str(n))
        self.functions[".".join(names)] = {"locals": {}}
        self.current_func = self.functions[".".join(names)]
        super(LuaTypesListener, self).visitFunctionDeclaration(ctx)
        self.current_func = {}

    #
    # def visitLocalVariableDecalaration(self, ctx: LuaParser.LocalVariableDecalarationContext):
    #     super(LuaTypesListener, self).visitLocalVariableDecalaration(ctx)
    #     atts = get_list(ctx.attnamelist().NAME())
    #     for att in atts:
    #         self.current_func["locals"][att.getText()] = {}
    #

    def visitVariableDeclaration(self, ctx: LuaParser.VariableDeclarationContext):
        vars = get_list(ctx.varlist().var_())
        explist = get_list(ctx.explist().exp())
        for j in range(len(vars)):
            var = vars[j]
            find_or_add_global(self.globals, self.current_func, str(var.NAME()), self.visit(explist[j]))

    def visitFunctioncall(self, ctx: LuaParser.FunctioncallContext):
        if ctx.varOrExp().getText() in inbuilt_functions:
            if ctx.nameAndArgs(0):
                argsLen = (len(ctx.nameAndArgs(0).args().explist().exp()))
                return getReturnType(ctx.varOrExp().getText(), argsLen)

    def visitExp(self, ctx: LuaParser.ExpContext):
        # super(LuaTypesListener, self).visitExp(ctx)
        if ctx.number():
            return self.visit(ctx.number())

        if ctx.string():
            return self.visit(ctx.string())

        if ctx.functiondef():
            return self.visit(ctx.functiondef())

        if ctx.prefixexp():
            return self.visit(ctx.prefixexp())

        # if ctx.tableconstructor():
        #     return "Table"
        #
        #
        #
        if ctx.operatorPeek():
            return {"type": "Any", "data": ctx.getText()}
        #

        # Arithmatic
        if ctx.operatorPower() or ctx.operatorMulDivMod() or ctx.operatorAddSub() or ctx.operatorBitwise():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))
            if x["type"] != "Number" or y["type"] != "Number":
                return {"type": "any", "data": ctx.getText()}
            return {"type": "Number", "data": ctx.getText()}

        if ctx.operatorUnary():
            x = self.visit(ctx.exp(0))
            if x["type"] != "Number":
                return {"type": "any", "data": ctx.getText()}
            return {"type": "Number", "data": ctx.getText()}

    def visitNumber(self, ctx: LuaParser.NumberContext):
        return {"type": "Number", "data": ctx.getText()}

    def visitString(self, ctx: LuaParser.StringContext):
        return {"type": "String", "data": ctx.getText()}

    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        if ctx.nameAndArgs():
            # is function call
            # check if is a inbuilt call
            if ctx.varOrExp().getText() in inbuilt_functions:
                if ctx.nameAndArgs(0):
                    argsLen = (len(ctx.nameAndArgs(0).args().explist().exp()))
                    return {"type": getReturnType(ctx.varOrExp().getText(), argsLen)}
        elif ctx.varOrExp():
            # this should be checked first incase a local variable is shadowing a function
            self.visit(ctx.varOrExp())
        return {"type": "Any"}

    # for now we ignore suffixes
    def visitVar_(self, ctx: LuaParser.Var_Context):
        return find_var(self.globals, self.current_func, str(ctx.NAME()))


def getReturnType(funcName, argsLen):
    argsList = inbuilt_functions[funcName]["args"]
    argsTable = {}
    for arg in argsList:
        argsTable[arg["argSize"]] = arg["type"]
    if argsLen in argsTable:
        return argsTable[argsLen]
    return argsTable[-1]


# for now we ignore suffixes
def find_var(globs, curr_func, name):
    if "locals" in curr_func:
        local = curr_func["locals"]
        if name in local:
            if "additional" in local[name]:
                return "Any"
            else:
                return local[name]["type"]
    if name in globs:
        if "additional" in globs[name]:
            return "Any"
        else:
            return globs[name]["type"]
    # throw error if not found anywhere
    raise Exception("THE FUCK , ERROR VAR USED BUT NOT FOUND")


# # This ignores . please fix
# def is_variable(listener: LuaTypesListener, varname, funcname):
#     if varname in listener.current_func:
#         return listener.current_func
#     elif varname in listener.globals:
#         return listener.globals[varname]


def find_or_add_global(globs, curr_func, name, addedType):
    if "locals" in curr_func:
        local = curr_func["locals"]
        if name in local:
            type = local[name]["type"]
            if type != addedType["type"]:
                globs[name]["additional"] = [addedType]
    elif name in globs:
        type = globs[name]["type"]
        if type != addedType["type"]:
            globs[name]["additional"] = [addedType]
    else:
        globs[name] = addedType


def get_list(thing):
    toRet = []
    for x in thing:
        toRet.append(x)
    return toRet


def get_code():
    code = ""
    in_code = False
    for line in open(sys.argv[1]):
        if "__lua__" in line:
            in_code = True
        elif "__gfx__" in line:
            in_code = False
        elif in_code:
            code += line + "\n"
    return code


def main():
    data = InputStream(get_code())
    # lexer
    lexer = LuaLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = LuaParser(stream)
    tree = parser.chunk()
    # evaluator
    visitor = LuaTypesListener()
    output = visitor.visit(tree)
    pprint(visitor.functions)
    pprint(visitor.globals)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print("provide a file")
