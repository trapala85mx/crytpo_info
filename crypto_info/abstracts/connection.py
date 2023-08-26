# Python
from abc import ABC, abstractmethod
# Project
# Externals
from peewee import PostgresqlDatabase, MySQLDatabase


class Connection(ABC):
    """Base class for a Database Connection
    """    
    _database: PostgresqlDatabase | MySQLDatabase = None
    
    def __init__(self) -> None:
        self._db_name: str = None
        self._user: str = None
        self._pasww: str = None
        self._host: str = None
        self._port: int = None
    
    @abstractmethod
    def _connect(self) -> PostgresqlDatabase | MySQLDatabase:
        """Make a connection to a Database via ORM
        
        returns:
            [PostgresqlDatabase | MySQLDatabase]: to be used for interact with Database
        """        
        pass
    
    @classmethod
    @abstractmethod
    def get_connection(cls) -> PostgresqlDatabase | MySQLDatabase:
        """Returns the connection to the Database
        returns:
            [PostgresqlDatabase | MySQLDatabase]: to be used for interact with Database
        """        
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Closes Database Connection
        """        
        pass