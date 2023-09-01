# Python
import uuid
# Project
from crypto_info.models.asset import Asset
from crypto_info.entities.asset_entity import AssetEntity
# Externals


class AssetService:
    
    def __init__(self, asset_entity: AssetEntity) -> None:
        self._asset_entity = asset_entity
    
    
    def insert_asset(self, asset:Asset) -> uuid:
        return self._asset_entity.insert_asset(asset=asset)
    
    
    def insert_many_assets(self, assets:list[Asset]) -> tuple:
        return self._asset_entity.insert_many_assets(assets=assets)
    
    
    def get_all_assets(self) -> list[Asset]:
        return self._asset_entity.get_all_assets()
    
    
    def delete_asset_by_symbol(self, symbol:str) -> int:
        return self._asset_entity.delete_asset_by_symbol(symbol=symbol.lower())
