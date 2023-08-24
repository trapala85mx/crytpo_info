# Python
# Project
from crypto_info import Asset
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


if __name__ == '__main__':
    run()