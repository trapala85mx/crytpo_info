# Python
import uuid
# Project
from crypto_info.models.asset import Asset
# Externals
from peewee import Model
from peewee import UUIDField, CharField, IntegerField
from peewee import PostgresqlDatabase, MySQLDatabase


class AssetEntity(Model):
        
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    symbol = CharField(max_length=20, unique=True, null=False,index=True)
    tick_size = CharField(max_length=20, unique=False, null=False)
    step_size = CharField(max_length=2, unique=False, null=False)
    min_qty = CharField(max_length=5, unique=False, null=False)
    min_cost = CharField(max_length=20, unique=False, null=False)
    max_leverage = CharField(max_length=4, unique=False, null=True)
    price_precision = IntegerField(null=False, unique=False)
    qty_precision = IntegerField(null=False, unique=False)
    price_factor = IntegerField(null=False, unique=False)
    qty_factor = IntegerField(null=False, unique=False)
        
    class Meta:
        database = None
        db_table = 'assets'
    
    @classmethod
    def initialize(cls, database: PostgresqlDatabase | MySQLDatabase) -> None:
        cls._meta.database = database
        