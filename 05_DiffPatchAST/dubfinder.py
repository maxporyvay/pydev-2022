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
    
    
