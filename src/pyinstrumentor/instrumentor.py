import inspect
import importlib
import pkgutil
from .core import instrument

def instrument_module(module):
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) or inspect.iscoroutinefunction(obj):
            setattr(module, name, instrument(obj))
        elif inspect.isclass(obj):
            for attr_name, attr_val in inspect.getmembers(obj):
                if inspect.isfunction(attr_val) or inspect.iscoroutinefunction(attr_val):
                    setattr(obj, attr_name, instrument(attr_val))

def instrument_package(package):
    instrument_module(package)
    if hasattr(package, '__path__'):
        for _, modname, _ in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            try:
                mod = importlib.import_module(modname)
                instrument_module(mod)
            except Exception:
                pass