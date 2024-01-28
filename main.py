import sys

from picotool.pico8.game.file import from_file
from picotool.pico8.tool import _printast_node


def main(filename):
    g = from_file(filename)
    _printast_node(g.lua.root)
    # print(g)


if __name__ == '__main__':
    # main(sys.argv[1])
    # main("demos-pico-8/comments.p8")
    main("demos-pico-8/assignment.p8")
