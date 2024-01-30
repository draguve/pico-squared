import sys

from Walker.BaseWalker import walk
from picotool.pico8.game.file import from_file
from picotool.pico8.tool import _printast_node


def main(filename):
    g = from_file(filename)
    _printast_node(g.lua.root)
    print("-" * 100)
    test = walk(g.lua.root, 0)
    print(test)
    with open("temp.txt", "w") as binary_file:
        binary_file.write(test)


if __name__ == '__main__':
    # main(sys.argv[1])
    # main("demos-pico-8/comments.p8")
    # main("demos-pico-8/assignment.p8")
    # main("demos-pico-8/simp_func.p8")
    # main("demos-pico-8/conditionals.p8")
    # main("demos-pico-8/loops.p8")
    main("demos-pico-8/tables.p8")
    # main("demos-pico-8/funcs.p8")
