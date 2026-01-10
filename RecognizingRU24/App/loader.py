# core/loader.py
import importlib
from types import ModuleType

from MGProjectRU25.Project.project_settings import BASE_PACKAGE


def qualify(dotted: str) -> str:
    # если путь не начинается с базового пакета — дополним
    if not dotted.split(".", 1)[0] == BASE_PACKAGE:
        return f"{BASE_PACKAGE}.{dotted}"
    return dotted


import importlib.util

print("find_spec('plugins') =", importlib.util.find_spec("plugins"))
print("CWD =", __import__("os").getcwd())
print("sys.path[:3] =", __import__("sys").path[:3])


def resolve_action(dotted: str):
    dotted = qualify(dotted)
    mod_path, func_name = dotted.rsplit(".", 1)
    module: ModuleType = importlib.import_module(mod_path)
    fn = getattr(module, func_name, None)
    if not callable(fn):
        raise AttributeError(f"Action '{dotted}' is not callable or missing")
    return fn
