from picotool.pico8.lua import lua
from Walker import BaseWalker
from Util import get_random_string, clamp


class PythonASTTransform(lua.BaseASTWalker):
    def __init__(self, tokens, root):
        self.all_functions = {}
        self.has_var_args = {}
        self.returns_shape = {}
        self.current_function_name = []
        self.returns_meta_data = {}
        super().__init__(tokens, root)

    def _walk_StatFunction(self, node):
        name_path = [BaseWalker.swalk_tok_name(name) for name in node.funcname.namepath]
        node.func_name = ".".join(BaseWalker.parser_return_lines(
            name_path))  # TODO this prob will be changed when i need to change the code for metatables
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
        last_number_of_args = None
        returns_shape_is_inconsistent = False
        all_returns = self.returns_shape[frozenset(self.current_function_name)]
        for i in range(0, len(all_returns)):
            if all_returns[i] is not None:
                if last_number_of_args is None:
                    last_number_of_args = len(all_returns[i].exps)
                elif last_number_of_args != len(all_returns[i].exps):
                    last_number_of_args = max(last_number_of_args, len(all_returns[i].exps))
                    returns_shape_is_inconsistent = True
                if all_returns[i] is not None:
                    for exp in all_returns[i].exps:
                        if type(exp).__name__ == "VarargDots":
                            returns_shape_is_inconsistent = True
            else:
                if last_number_of_args is None:
                    last_number_of_args = 0
                elif last_number_of_args != 0:
                    last_number_of_args = max(last_number_of_args, 0)
                    returns_shape_is_inconsistent = True
        if last_number_of_args is None:
            last_number_of_args = 0
        self.returns_meta_data[frozenset(self.current_function_name)] = (
            returns_shape_is_inconsistent, last_number_of_args)

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
