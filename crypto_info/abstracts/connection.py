# Python
from abc import ABC, abstractmethod
# Project
# Externals


class Connection(ABC):
    
    def __init__(self) -> None:
        self._db_name = None
        self._user = None
        self._pasww = None
        self._host = None
        self._port = None
    
    @abstractmethod
    def _connect(self):
        pass
    
    @classmethod
    @abstractmethod
    def get_orm(cls):
        pass
    
    @abstractmethod
    def close(self):
        pass