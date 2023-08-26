# Python
from crypto_info.abstracts.connection import Connection

# Project
from crypto_info.utils.decorators import singleton
# Externals
from decouple import config
from peewee import PostgresqlDatabase


@singleton
class PostgreSQLConnection(Connection):
    """Class to create a PostreSQL Connection with ORM
    """    
    def __init__(self) -> None:
        self._db_name: str = config("CRYPTO_INFO_DB_NAME")
        self._user: str = config("CRYPTO_INFO_DB_USER")
        self._pasww: str = config("CRYPTO_INFO_DB_PASS")
        self._host: str = config("CRYPTO_INFO_DB_HOST")
        self._port: int = config("CRYPTO_INFO_DB_PORT")

    def _connect(self) -> PostgresqlDatabase:
        """Connect to PostgreSQÑ Database using the ORM

        Returns:
            PostgresqlDatabase: Connection to PostgreSQL Database where data is stored
        """        
        return PostgresqlDatabase(
            self._db_name,
            user=self._user,
            password=self._pasww,
            host=self._host,
            port=self._port,
        )

    @classmethod
    def get_connection(cls) -> PostgresqlDatabase:
        """Public method to get the connection with Database. If connection exists return the connection if not,
        the connection is created

        Returns:
            PostgresqlDatabase: Connection to PostgreSQL database
        """        
        if cls._database is None:
            cls._database = cls()._connect()
        
        return cls._database

    def close(self) -> None:
        """Close connection to PostgreSQL Database
        """        
        self._database.close()
