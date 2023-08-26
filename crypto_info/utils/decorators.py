# Python
import functools
# Project
# Externals


def singleton(cls) -> function:
    """Class Decorator to apply Singleton

    Returns:
        function: function that will be executed instead of the one that is being decorated
    """    
    _instances = {}
    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        """Wraps that will search for the instance and returns it

        Returns:
            [type]: The class with its args / kwargs
        """        
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper