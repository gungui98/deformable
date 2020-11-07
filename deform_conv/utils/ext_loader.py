import importlib
import pkgutil


def load_ext(name, funcs):
    ext = importlib.import_module('deform_conv.' + name)
    for fun in funcs:
        assert hasattr(ext, fun), f'{fun} miss in module {name}'
    return ext

def check_ops_exist():
    ext_loader = pkgutil.find_loader('deform_conv._ext')
    return ext_loader is not None
