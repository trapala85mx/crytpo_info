# Python
from crypto_info.abstracts.connection import Connection
# Project
# Externals
from decouple import config
from peewee import PostgresqlDatabase

class PostgreSQLConnection(Connection):
        
    def __init__(self) -> None:
        self._db_name = config('CRYPTO_INFO_DB_NAME')
        self._user = config('CRYPTO_INFO_DB_USER')
        self._pasww = config('CRYPTO_INFO_DB_PASS')
        self._host = config('CRYPTO_INFO_DB_HOST')
        self._port = config('CRYPTO_INFO_DB_PORT')
    
    def _create_connection(self):
        if self._con:
            return self._con
        
        return PostgresqlDatabase(
            self._db_name, 
            user=self._user, 
            password=self._pasww,
            host=self._host, 
            port=self._port)
    
    @classmethod
    def get_connection(self):
        self._con = self._create_connection()
        return self._con
    
    def close(self):
        if self._con:
            self._con.close()