from picotool.pico8.lua import lua
from Walker import BaseWalker
from Util import get_random_string, clamp


class PythonASTTransform(lua.BaseASTWalker):
    def __init__(self, tokens, root):
        self.all_functions = {}
        self.has_var_args = {}
        self.returns_shape = {}
        self.current_function_name = []
        super().__init__(tokens, root)

    def _walk_StatFunction(self, node):
        name_path = [BaseWalker.swalk_tok_name(name) for name in node.funcname.namepath]
        node.func_name = ".".join(BaseWalker.parser_return_lines(name_path))  # TODO this prob will be changed when i need to change the code for metatables
        self.current_function_name.append(".".join(BaseWalker.parser_return_lines(name_path)))
        for i in lua._default_node_handler(self, node):
            yield i
        self.current_function_name.pop()

    def _walk_FunctionBody(self, node):
        args = []
        set_name = frozenset(self.current_function_name)
        self.has_var_args[set_name] = False
        self.returns_shape[set_name] = []
        if node.parlist is not None:
            args.extend(node.parlist.names)
        if node.dots is not None:
            args.append(node.dots)
            self.has_var_args[set_name] = True
        self.all_functions[set_name] = args
        for i in lua._default_node_handler(self, node):
            yield i

    def _walk_StatReturn(self, node):
        set_name = frozenset(self.current_function_name)
        self.returns_shape[set_name].append(node.explist)
        for i in lua._default_node_handler(self, node):
            yield i

    def _walk_Function(self, node):
        func_name = f"anon_{get_random_string(10)}"
        node.func_name = func_name
        self.current_function_name.append(func_name)
        for i in lua._default_node_handler(self, node):
            yield i
        self.current_function_name.pop()

    # def _walk_FunctionArgs(self, node):
    #     for i in lua._default_node_handler(self, node):
    #         yield i
