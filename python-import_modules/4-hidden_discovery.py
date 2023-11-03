#!/usr/bin/python3
import ast
b = []
if __name__ == '__main__':
    with open('hidden_4.py') as f:
        tree = f.read()
        module = ast.parse(tree)
        functions = [node for node in module.body if isinstance(node, ast.FunctionDef)]
        for f in functions:
            a = str(f.name)
            if a.startswith('__'):
                pass
            else:
                b.append(a)
        b = sorted(b)
        for i in range(len(b)):
            print(b[i])
