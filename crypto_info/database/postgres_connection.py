# Python
from crypto_info.abstracts.connection import Connection

# Project
# Externals
from decouple import config
from peewee import PostgresqlDatabase


class PostgreSQLConnection(Connection):
    def __init__(self) -> None:
        self._db_name: str = config("CRYPTO_INFO_DB_NAME")
        self._user: str = config("CRYPTO_INFO_DB_USER")
        self._pasww: str = config("CRYPTO_INFO_DB_PASS")
        self._host: str = config("CRYPTO_INFO_DB_HOST")
        self._port: int = config("CRYPTO_INFO_DB_PORT")

    def _connect(self) -> PostgresqlDatabase:
        return PostgresqlDatabase(
            self._db_name,
            user=self._user,
            password=self._pasww,
            host=self._host,
            port=self._port,
        )

    @classmethod
    def get_connection(cls) -> PostgresqlDatabase:
        if cls._database is None:
            cls._database = cls()._connect()
        
        return cls._database

    def close(self):
        self._database.close()
