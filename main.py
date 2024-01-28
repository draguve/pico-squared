import sys
from antlr4 import *
from LuaAntlr.LuaLexer import LuaLexer
from LuaAntlr.LuaParser import LuaParser


def main():
    input_file = open(sys.argv[1], 'r').read()

    lexer = LuaLexer(input_file)
    tokens = CommonTokenStream(lexer)
    parser = LuaParser(tokens)
    tree = parser.chunk()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()

