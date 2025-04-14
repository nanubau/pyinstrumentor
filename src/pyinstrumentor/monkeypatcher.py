import ast
import os
import importlib
from .core import instrument

def find_imported_functions(file_path):
    with open(file_path) as f:
        tree = ast.parse(f.read(), filename=file_path)
    imported_funcs = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            mod = node.module
            for alias in node.names:
                imported_funcs.append((mod, alias.name))
    return imported_funcs

def monkey_patch_third_party(root_dir):
    patched = set()
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                funcs = find_imported_functions(os.path.join(root, file))
                for modname, funcname in funcs:
                    try:
                        mod = importlib.import_module(modname)
                        if hasattr(mod, funcname) and (modname, funcname) not in patched:
                            setattr(mod, funcname, instrument(getattr(mod, funcname)))
                            patched.add((modname, funcname))
                    except Exception:
                        continue