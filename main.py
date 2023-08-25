# Python
# Project
from crypto_info import Asset
from crypto_info.entities.asset_entity import AssetEntity
from crypto_info.database.postgres_connection import PostgreSQLConnection
# Externals


def run():
    data = {
        'tick_size': '0.00001',
        'step_size': '1',
        'min_qty': '39',
        'min_cost': '5.12070'
    }
    asset = Asset(
        symbol='suiusdt',
        tick_size = data["tick_size"],
        step_size = data['step_size'],
        min_qty = data['min_qty'],
        min_cost = data['min_cost']
    )
    asset.max_leverage = '10'
    asset.price_factor = 1
    asset.qty_factor = 1
    asset.price_precision = 0
    asset.qty_precision = 2
    
    print(asset)

    db = PostgreSQLConnection().get_connection()
    print(db)
    AssetEntity.initialize(db)
    AssetEntity.create_table()
    AssetEntity.create(
        symbol = asset.symbol,
        tick_size = asset.tick_size,
        step_size = asset.step_size,
        min_qty = asset.min_qty,
        min_cost = asset.min_cost,
        max_leverage = asset.max_leverage,
        price_precision = asset.price_precision,
        qty_precision = asset.qty_precision,
        price_factor = asset.price_factor,
        qty_factor = asset.qty_factor
    )
    
    db.close()

if __name__ == '__main__':
    run()
    '''
    class A(object):
        def __new__(cls, *args, **kwargs):
            print("Creating instance")
            #return super(A, cls).__new__(cls)
            return object.__new__(cls, *args, **kwargs)
    
        def __init__(self):
            print("Init is called")
  
    A()
    '''