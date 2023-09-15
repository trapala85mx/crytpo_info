# Python
import uuid
import math
import re
# Project
from crypto_info.models.asset import Asset
from crypto_info.entities.asset_entity import AssetEntity
# Externals


class AssetService:
    
    def __init__(self, asset_entity: AssetEntity) -> None:
        self._asset_entity = asset_entity
    
    
    def insert_asset(self, asset:Asset) -> uuid:
        return self._asset_entity.insert_asset(asset=asset)
    
    
    def insert_many_assets(self, assets:list[Asset]) -> bool:
        self._asset_entity.insert_many_assets(assets=assets)
        return True
    
    
    def get_all_assets(self) -> list[Asset]:
        return self._asset_entity.get_all_assets()
    
    
    def delete_asset_by_symbol(self, symbol:str) -> int:
        return self._asset_entity.delete_asset_by_symbol(symbol=symbol.lower())
    
    
    def set_attributes(self, asset:Asset):
        asset.price_precision = self._price_precision(asset)
        asset.qty_precision = self._qty_precision(asset)
        asset.price_factor = self._price_factor(asset.price_precision)
        asset.qty_factor = self._qty_factor(asset.qty_precision)
    
    
    def _price_precision(self, asset:Asset) -> int:
        decimals: list = self._split_decimals(asset.priceFilter_tickSize)
        precision: int = self._get_precision(decimals)
        return int(precision)
    
    
    def _qty_precision(self, asset:Asset) -> None:
        decimals: list = self._split_decimals(asset.lotSizeFilter_stepSize)
        precision: int = self._get_precision(decimals)
        return int(precision)
    
    
    def _price_factor(self, price_precision:int):
        return 10**price_precision
    
    
    def _qty_factor(self, qty_precision:int):
        return 10**qty_precision
    
    
    def _split_decimals(self, ticksize:str) -> list:
        m = re.match(r'^0.[0]*1', ticksize)
        if m:
            result = m.string[2:]
        else:
            result = []
        return result
    
    def _get_precision(self, decimals:str) -> int:
        if len(decimals) == 0:
            return 0
    
        res = re.split(r'1', decimals)
        return len(res[0])+1