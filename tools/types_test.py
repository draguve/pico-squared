import sys
from antlr4 import *

from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaVisitor import LuaVisitor
from LuaListener import LuaListener
from pprint import pprint


class LuaTypesListener(LuaListener):
    def __init__(self):
        self.current_func = None
        self.globals = {}
        self.functions = {}

    # What about local functions
    def enterFunctionDeclaration(self, ctx: LuaParser.FunctionDeclarationContext):
        names = []
        name = ctx.funcname().NAME()
        for n in name:
            names.append(str(n))
        self.functions[".".join(names)] = {"locals": {}}
        self.current_func = ".".join(names)

    def exitFunctionDeclaration(self, ctx: LuaParser.FunctionDeclarationContext):
        self.current_func = None

    def exitLocalVariableDecalaration(self, ctx: LuaParser.LocalVariableDecalarationContext):
        atts = get_list(ctx.attnamelist().NAME())
        for att in atts:
            self.functions[self.current_func]["locals"][att.getText()] = {}

    def exitVariableDeclaration(self, ctx: LuaParser.VariableDeclarationContext):
        vars = get_list(ctx.varlist().var_())
        for var in vars:
            suffixes = [str(i.NAME()) for i in get_list(var.varSuffix())]
            find_or_add(self.globals, self.functions[self.current_func]["locals"], str(var.NAME()), suffixes)
    # check and add all returns of type in a function
    # what happens when it returns a nil

    # check what happens when a variable is used
    # expression parsing


# This ignores . please fix
def is_variable(listener: LuaTypesListener, varname, funcname):
    if varname in listener.functions[listener.current_func]:
        return listener.functions[listener.current_func]
    elif varname in listener.globals:
        return listener.globals[varname]


def find_or_add(globs, local, name, suffixes):
    if name in local:
        final = local[name]
        for suffix in suffixes:
            if suffix in final:
                final = final[suffix]
            else:
                final[suffix] = {}
                final = final[suffix]
    elif name in globs:
        final = globs[name]
        for suffix in suffixes:
            if suffix in final:
                final = final[suffix]
            else:
                final[suffix] = {}
                final = final[suffix]
    else:
        globs[name] = {}
        final = globs[name]
        for suffix in suffixes:
            final[suffix] = {}
            final = final[suffix]
    pass


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
    listener = LuaTypesListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    pprint(listener.functions)
    pprint(listener.globals)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print("provide a file")
