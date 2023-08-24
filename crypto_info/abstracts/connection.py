# Python
from abc import ABC, abstractmethod
# Project
# Externals


class Connection(ABC):
    
    _con = None
    
    def __init__(self) -> None:
        pass    
    
    @abstractmethod
    def _create_connection(self):
        pass
    
    @abstractmethod
    @classmethod
    def get_connection(self):
        pass
    
    @abstractmethod
    def close(self):
        pass