# Python
from abc import ABC, abstractmethod
# Project
# Externals
from peewee import PostgresqlDatabase, MySQLDatabase


class Connection(ABC):
    
    _database: PostgresqlDatabase | MySQLDatabase = None
    
    def __init__(self) -> None:
        self._db_name: str = None
        self._user: str = None
        self._pasww: str = None
        self._host: str = None
        self._port: int = None
    
    @abstractmethod
    def _connect(self) -> PostgresqlDatabase | MySQLDatabase:
        pass
    
    @classmethod
    @abstractmethod
    def get_connection(cls) -> PostgresqlDatabase | MySQLDatabase:
        pass
    
    @abstractmethod
    def close(self) -> None:
        pass