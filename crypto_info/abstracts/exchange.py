# Python
from abc import ABC, abstractmethod

# Project
from crypto_info.models.asset import Asset
from crypto_info.services.asset_service import AssetService

# Externals


class Exchange(ABC):
    
    def __init__(self, asset_service: AssetService) -> None:
        self._asset_service = asset_service
        
        
    @abstractmethod
    def futures_exchange_info(self) -> dict:
        pass
    
    
    @abstractmethod
    def get_24hr_change_statistics(self, symbol=None) -> dict | list[dict]:
        pass
    
    
    @abstractmethod
    async def save_assets_info(self) -> list[dict]:
        pass