# Python
# Project
from crypto_info import Asset
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
        tick_size = data["tick_size"],
        step_size = data['step_size'],
        min_qty = data['min_qty'],
        min_cost = data['min_cost']
    )
    print(asset)

    db = PostgreSQLConnection().get_connection()
    print(db)
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