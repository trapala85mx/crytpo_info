# Python
import uuid

# Project
from crypto_info.models.asset import Asset

# Externals
import psycopg2
import peewee
from peewee import Model
from peewee import UUIDField, CharField, IntegerField
from peewee import PostgresqlDatabase, MySQLDatabase


class AssetEntity(Model):
    """Class for mapping an Asset to Database using ORM"""

    id = UUIDField(primary_key=True, default=uuid.uuid4)
    symbol = CharField(max_length=20, unique=True, null=False, index=True)
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
        db_table = "assets_info"

    @classmethod
    def initialize(cls, database: PostgresqlDatabase | MySQLDatabase) -> None:
        """Set needed databse connection to work properly using the param injected
        Args:
            database (PostgresqlDatabase): Connection to PostgreSQL Databse
        """
        cls._meta.database = database
    
    
    def insert_asset(cls, asset: Asset) -> bool:
        """Insert an Asset into the Database
        Args:
            asset (Asset): Assset to be stored in Database
        Returns:
            uuid: id(Primary Key) of the asset stored
        """
        try:
            res = AssetEntity.insert(**asset.__dict__).execute()
        
        except peewee.OperationalError as err:
            print(f"Couldn't insert data for {asset.symbol.upper()}")
            print(err)
        
        except peewee.IntegrityError as e:
            print(f"Error in insert many assets")
            print(e)
        
        except psycopg2.errors.UniqueViolation as e:
            print(e)
        
        else:
            if res:
                return True
            
            return False

    def insert_many_assets(cls, assets: list[Asset]) -> bool:
        """Insert many Assets into Database
        Args:
            assets (list[Asset]): List of Assets
        Raises:
            ValueError: If List of Assets == 0
        Returns:
            bool: Tru if assets where inserted Flase if they were not
        """
        if len(assets) == 0:
            raise ValueError("You didn't send any data to store")
        
        try:
            data = [a.__dict__ for a in assets]
            res = AssetEntity.insert_many(data).execute()
        
            if res:
                return True
            
            return False
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print("Couldn't insert assets")
            print(e)
        
        except peewee.IntegrityError as e:
            print(f"Error in insert many assets")
            print(e)
        
        except psycopg2.errors.UniqueViolation as e:
            print(e)
    
    
    def get_all_assets(cls) -> list[Asset]:
        """Retrieves all Assets from Datbase
        Raises:
            ValueError: If there are no Assets in DataBase
        Returns:
            list[Asset]: List of all Assets in Database
        """
        try:
            res = AssetEntity.select()
            if res > 0:
                return res
            raise ValueError("No data to extract")
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print("Something went wrong retrieving all Assets")
    
    
    def update_asset(cls, data: dict) -> bool:
        """Update an asset in database
        Args:
            data (dict): Dict with all atributes/cols to be updated
        Raises:
            ValueError: If no data is sent
        Returns:
            bool: True if asset is updated False if not
        """
        if len(data) == 0:
            raise ValueError("You didn't send data to updated")
        
        try:
            nrows = (
                AssetEntity.update(**data)
                .where(AssetEntity.symbol == data["symbol"].lower())
                .execute()
            )
            
            if nrows >= 1:
                return True
            return False
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print(f"Couln't update data for {data['symbol'].upper()}")
            print(e)
    
    
    def delete_asset_by_symbol(cls, symbol: str) -> bool:
        """Delete an Asset based in symbl
        Args:
            symbol (str): Asset Symbol to be deleted in Database
        Raises:
            ValueError: If no Symbol is sent
        Returns:
            bool: True if asset is deleted False if not
        """
        if len(symbol) == 0:
            raise ValueError("You didn't send a symbol")
        
        try:
            nrows = (
                AssetEntity.delete()
                .where(AssetEntity.symbol == symbol.lower())
                .execute()
            )
            
            if nrows == 1:
                return True
            return False
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print(f"Couldn't delete {symbol.upper()}")
            print(e)
