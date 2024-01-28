from picotool.pico8.lua import lua


class PythonASTTransform(lua.LuaASTEchoWriter):
    def __init__(self, tokens, root):
        super().__init__(tokens, root)

    def _get_text(self, node, keyword):
        """Gets the preceding spaces and code for a TokKeyword or TokSymbol.

        Args:
          node: The Node containing the keyword.
          keyword: The expected keyword or symbol.

        Returns:
          The text for the keyword or symbol.
        """
        if self._args.get('ignore_tokens'):
            return b' ' + keyword

        spaces = self._get_code_for_spaces(node)
        self._pos += 1
        return spaces + keyword

    def _walk_StatGoto(self, node):
        raise NotImplementedError("Dont know how to yet")

    def _walk_StatLabel(self, node):
        raise NotImplementedError("Dont know how to yet")

    def _walk_ExpValue(self, value):
        yield b"??"

    def _walk_StatAssignment(self, node):
        for t in self._walk(node.varlist):
            yield t
        yield self._get_text(node, node.assignop.code)
        for t in self._walk(node.explist):
            yield t
