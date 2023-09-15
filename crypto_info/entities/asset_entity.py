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
    priceFilter_minPrice = CharField(max_length=20, null=False)
    priceFilter_maxPrice = CharField(max_length=20, null=False)
    priceFilter_tickSize = CharField(max_length=20, null=False)
    lotSizeFilter_minQty = CharField(max_length=20, null=False)
    lotSizeFilter_maxQty = CharField(max_length=20, null=False)
    lotSizeFilter_stepSize = CharField(max_length=5, null=False)
    marketLotSizeFilter_minQty = CharField(max_length=20, null=False)
    marketLotSizeFilter_maxQty = CharField(max_length=20, null=False)
    marketLotSizeFilter_stepSize = CharField(max_length=5, null=False)
    minNotionalFilter_notional = CharField(max_length=5, null=False)
    percentPriceFilter_multiplierUp = CharField(max_length=10, null=False)
    percentPriceFilter_multiplierDown = CharField(max_length=10, null=False)
    percentPriceFilter_multiplierDecimal = IntegerField(null=False)
    price_precision = IntegerField(null=False, unique=False)
    qty_precision = IntegerField(null=False, unique=False)
    price_factor = IntegerField(null=False, unique=False)
    qty_factor = IntegerField(null=False, unique=False)

    class Meta:
        database = None
        db_table = "assets_info"

    
    def __str__(self):
        return self.symbol.upper()
    
    
    @classmethod
    def initialize(cls, database: PostgresqlDatabase | MySQLDatabase) -> None:
        """Set needed databse connection to work properly using the param injected
        Args:
            database (PostgresqlDatabase): Connection to PostgreSQL Databse
        """
        cls._meta.database = database
    
    
    def insert_asset(self, asset: Asset) -> uuid:
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
            return res
    

    def insert_many_assets(self, assets: list[Asset]) -> tuple:
        """Insert many Assets into Database
        Args:
            assets (list[Asset]): List of Assets
        Raises:
            ValueError: If List of Assets == 0
        Returns:
            tuple: Tuple of uuid / ids of each Asset inserted into DataBase
        """
        if len(assets) == 0:
            raise ValueError("You didn't send any data to store")
        
        try:
            data = [a.__dict__ for a in assets]
            res = AssetEntity.insert_many(data).execute()
        
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
        
        else:
            return res
    
    
    def get_all_assets(self) -> list[Asset]:
        """Retrieves all Assets from Datbase
        Raises:
            ValueError: If there are no Assets in DataBase
        Returns:
            list[Asset]: List of all Assets in Database
        """
        try:
            res = AssetEntity.select()
            assets = []
            if res > 0:
                for crypto in res:
                    assets.append(crypto)
                return assets
            raise ValueError("No data to extract")
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print("Something went wrong retrieving all Assets")
            
    
    def delete_asset_by_symbol(clselfs, symbol: str) -> int:
        """Delete an Asset based in symbl
        Args:
            symbol (str): Asset Symbol to be deleted in Database
        Raises:
            ValueError: If no Symbol is sent
        Returns:
            int: number of rows deleted
        """
        if len(symbol) == 0:
            raise ValueError("You didn't send a symbol")
        
        try:
            nrows = (
                AssetEntity.delete()
                .where(AssetEntity.symbol == symbol.lower())
                .execute()
            )
            
            if nrows > 0:
                return True
            
        
        except ValueError as e:
            print(e)
        
        except peewee.OperationalError as e:
            print(f"Couldn't delete {symbol.upper()}")
            print(e)
