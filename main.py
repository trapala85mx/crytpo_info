# Python
import asyncio

# Project
from crypto_info.entities.asset_entity import AssetEntity

from crypto_info.services.binance import Binance
from crypto_info.services.asset_service import AssetService

from crypto_info.database.postgres_connection import PostgreSQLConnection

# Externals


async def run():
    try:
        db = PostgreSQLConnection().get_connection()
        
        asset_entity = AssetEntity()
        AssetEntity.initialize(db)
        AssetEntity.drop_table()
        AssetEntity.create_table()
        
        asset_service = AssetService(asset_entity=asset_entity)
        exchange = Binance(asset_service=asset_service)
        
        saved = await exchange.save_assets_info()
        if not saved:
            raise ValueError("Couln't save data")
        
        print("Data Extracted and Saved Succesfully")
    
    except ValueError as e:
        print(e)
    finally:
        db.close()

if __name__ == '__main__':
    asyncio.run(run())
