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
    asset1 = Asset(
        symbol='suiusdt',
        tick_size = data["tick_size"],
        step_size = data['step_size'],
        min_qty = data['min_qty'],
        min_cost = data['min_cost']
    )
    asset1.max_leverage = '10'
    asset1.price_factor = 1
    asset1.qty_factor = 1
    asset1.price_precision = 0
    asset1.qty_precision = 2
    asset2 = Asset(
        symbol='maticusdt',
        tick_size = data["tick_size"],
        step_size = data['step_size'],
        min_qty = data['min_qty'],
        min_cost = data['min_cost']
    )
    asset2.max_leverage = '10'
    asset2.price_factor = 1
    asset2.qty_factor = 1
    asset2.price_precision = 0
    asset2.qty_precision = 2
    
    db = PostgreSQLConnection().get_connection()
    
    AssetEntity.initialize(db)
    AssetEntity.drop_table()
    AssetEntity.create_table()
    
    #res = AssetEntity.create_asset(asset1)
    res = AssetEntity.create_many_assets([asset1, asset2])
    
    #res = AssetEntity.create_asset(asset2)
    asset2.max_leverage = '20'
    res = AssetEntity.update_asset(asset2.__dict__)
    #print(res)
    assets = AssetEntity.get_all_assets()
    for a in assets:
        print(a.symbol, " - ",a.price_factor)
    
    res = AssetEntity.delete_asset_by_symbol("maticusdt")
    print(res)
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