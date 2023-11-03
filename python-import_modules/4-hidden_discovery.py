#!/usr/bin/python3
import uncompyle6, ast
if __name__ == '__main__':
    with open('hidden_4.py', 'w') as f:
        uncompyle6.decompile_file('hidden_4.pyc', f)
with open('hidden_4.py') as f:
    tree = f.read()
module = ast.parse(tree)
function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]
for f in function_definitions:
    a = str(f.name)
    b = []
    if a.startswith('__'):
        pass
    else:
        b.append(a)
        b.sort()
    for i in range(len(b)):
        print(b[i])
        
