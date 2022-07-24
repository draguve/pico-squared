import sys
from antlr4 import *

from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaVisitor import LuaVisitor
from pprint import pprint


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
        super().visitFunctionDeclaration(ctx)
        self.current_func = {}

    def visitLocalVariableDecalaration(self, ctx: LuaParser.LocalVariableDecalarationContext):
        super(LuaTypesListener, self).visitLocalVariableDecalaration(ctx)
        atts = get_list(ctx.attnamelist().NAME())
        for att in atts:
            self.current_func["locals"][att.getText()] = {}

    def visitVariableDeclaration(self, ctx: LuaParser.VariableDeclarationContext):
        super(LuaTypesListener, self).visitVariableDeclaration(ctx)
        vars = get_list(ctx.varlist().var_())
        for var in vars:
            suffixes = [str(i.NAME()) for i in get_list(var.varSuffix())]
            find_or_add(self.globals, self.current_func["locals"], str(var.NAME()), suffixes)

    def visitExp(self, ctx: LuaParser.ExpContext):
        super(LuaTypesListener, self).visitExp(ctx)
        if ctx.number():
            return "Number"

        if ctx.string():
            return "String"

        if ctx.functiondef():
            return "Func"

        if ctx.prefixexp():
            print(f"prefix exp -- {ctx.getText()}")

        if ctx.tableconstructor():
            return "Table"

        if ctx.operatorUnary():
            return "Number"

        if ctx.exp():
            self.visit(ctx.exp(0))

        if ctx.operatorPeek():
            return "Number"

        if ctx.operatorPower():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorMulDivMod():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorAddSub():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorStrcat():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorComparison():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))
            return "Boolean"

        if ctx.operatorAnd():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorOr():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))

        if ctx.operatorBitwise():
            x = self.visit(ctx.exp(0))
            y = self.visit(ctx.exp(1))
            return "Number"

    def visitNumber(self, ctx: LuaParser.NumberContext):
        return "Number"

    def visitString(self, ctx: LuaParser.StringContext):
        return "String"

    def visitTableconstructor(self, ctx: LuaParser.TableconstructorContext):
        return "Table"

    # check and add all returns of type in a function
    # what happens when it returns a nil

    # check what happens when a variable is used
    # expression parsing


# This ignores . please fix
def is_variable(listener: LuaTypesListener, varname, funcname):
    if varname in listener.current_func:
        return listener.current_func
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
    visitor = LuaTypesListener()
    output = visitor.visit(tree)
    pprint(visitor.functions)
    pprint(visitor.globals)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print("provide a file")
