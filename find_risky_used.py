import ast


class RiskyFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.risky_functions = []
        self.RISKY_FUNCTIONS = [
            'os.system',
            'subprocess.call',
            'pickle.loads',
            'eval',
            'exec',
        ]

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            module_name = node.func.value.id if isinstance(node.func.value, ast.Name) else None
            function_name = node.func.attr
        else:
            module_name = None
            function_name = node.func.id

        if function_name in self.RISKY_FUNCTIONS:
            self.risky_functions.append((module_name, function_name))

        self.generic_visit(node)

class RiskyLibraryVisitor(ast.NodeVisitor):
    def __init__(self):
        self.risky_libraries = []
        self.RISKY_LIBRARIES = [
            'pickle',
            'os',
            'subprocess',
            'paramiko',
            # Add more risky libraries here
        ]

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name in self.RISKY_LIBRARIES:
                self.risky_libraries.append(alias.name)

    def visit_ImportFrom(self, node):
        if node.module in self.RISKY_LIBRARIES:
            self.risky_libraries.append(node.module)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            module_name = node.func.value.id
        else:
            module_name = None

        if module_name in self.RISKY_LIBRARIES:
            self.risky_libraries.append(module_name)

        self.generic_visit(node)


def find_risky_functions_and_libraries(code: str) -> tuple[str, str]:
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return [], []

    function_visitor = RiskyFunctionVisitor()
    function_visitor.visit(tree)

    library_visitor = RiskyLibraryVisitor()
    library_visitor.visit(tree)

    risky_functions = " ".join([f"{module}.{function}" if module else function for module, function in set(function_visitor.risky_functions)])
    risky_libraries = " ".join(set(library_visitor.risky_libraries))

    return risky_functions, risky_libraries


### For Example ###

code = """
import os
from pickle import loads
import subprocess

os.system('rm -rf /')
subprocess.call(['ls', '-la'])
data = loads(pickled_data)
"""


risky_functions, risky_libraries = find_risky_functions_and_libraries(code)

print(f"Risky functions: {risky_functions}")
print(f"Risky libraries: {risky_libraries}")

