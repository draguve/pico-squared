import sys
from antlr4 import *

from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaVisitor import LuaVisitor


class TypeLuaParser(LuaVisitor):
    def __init__(self):
        self.globals = {}
        self.functions = {}

    def visitVariableDeclaration(self, ctx: LuaParser.VariableDeclarationContext):
        vars = self.visit(ctx.varlist())
        exps = self.visit(ctx.explist())
        # print(ctx.getText())

    def visitFuncname(self, ctx:LuaParser.FuncnameContext):
        print(ctx.getText())
        return ctx.getText()

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
    visitor = TypeLuaParser()
    output = visitor.visit(tree)
    print(output)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print("provide a file")
