# Python
import functools
# Project
# Externals


def singleton(cls):
    
    _instances = {}
    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper