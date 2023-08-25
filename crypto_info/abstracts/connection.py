# Python
from abc import ABC, abstractmethod
# Project
# Externals
from peewee import PostgresqlDatabase, MySQLDatabase


class Connection(ABC):
    
    _database: PostgresqlDatabase | MySQLDatabase = None
    
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
    def get_connection(cls):
        pass
    
    @abstractmethod
    def close(self):
        pass