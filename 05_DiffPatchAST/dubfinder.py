import importlib
import ast
import inspect
import difflib
import textwrap
import sys

funcdict = {}


def myInspect(item, prefix):
    for name, value in inspect.getmembers(item):
        if inspect.isfunction(value):
            funcdict[prefix + name] = value
        elif inspect.isclass(value) and (len(name) == 1 or name[:2] != '__'):
            myInspect(value, prefix + name + '.')


for modidx in range(1, len(sys.argv)):
    modulename = sys.argv[modidx]
    module = importlib.import_module(modulename)
    myInspect(module, modulename + '.')

for k, v in funcdict.items():
    text = textwrap.dedent(inspect.getsource(v))
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if 'name' in dir(node):
            node.name = '_'
        if 'id' in dir(node):
            node.id = '_'
        if 'attr' in dir(node):
            node.attr = '_'
        if 'arg' in dir(node):
            node.arg = '_'
    modifiedtext = ast.unparse(tree)
    funcdict[k] = modifiedtext

pairs = []

for k, v in funcdict.items():
    maxratio = -1
    pos = -1
    for k1, v1 in funcdict.items():
        if k != k1:
            ratio = difflib.SequenceMatcher(None, v, v1).ratio()
            if ratio > maxratio:
                maxratio = ratio
                pos = k1
    if maxratio > 0.95 and (pos, k) not in pairs:
        pairs.append((k, pos))

for k1, k2 in sorted(pairs):
    print(k1, k2, sep=' : ')
            
    
