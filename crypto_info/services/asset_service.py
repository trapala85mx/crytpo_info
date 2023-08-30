# Python
# Project
from crypto_info.models.asset import Asset
from crypto_info.entities.asset_entity import AssetEntity
# Externals


class AssetService:
    
    def __init__(self, asset_entity: AssetEntity) -> None:
        self._asset_entity = asset_entity
    
    
    def insert_asset(self, asset:Asset):
        self._asset_entity.insert_asset(asset=asset)
    
    
    def insert_many_assets(self, assets:list[Asset]):
        self._asset_entity.insert_many_assets(assets=assets)
    
    
    def delete_asset_by_symbol(self, symbol:str):
        self._asset_entity.delete_asset_by_symbol(symbol=symbol.lower())
    
    
    async def _create_assets(self, data: list[dict]) -> list[Asset]:
        tasks = []
        
        for d in data:
            symbol = d["symbol"].lower()
            
            a = Asset(
                symbol=symbol, tick_size="", step_size="", min_qty="", min_cost=""
            )