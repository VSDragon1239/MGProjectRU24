# core/registry.py
from typing import Callable, Dict

_registry: Dict[str, Callable] = {}


def command(name: str):
    def wrap(fn: Callable):
        _registry[name] = fn
        return fn

    return wrap


def get_registered(name: str) -> Callable | None:
    return _registry.get(name)
