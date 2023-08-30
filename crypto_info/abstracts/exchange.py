# Python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, Field
# Project
from crypto_info.models.asset import Asset
from crypto_info.entities.asset_entity import AssetEntity
# Externals

@dataclass(kw_only=True)
class Exchange(ABC):
    
    asset_entity: AssetEntity = field(default=None)
    
    @classmethod
    def _get_futures_exchange_info(self) -> dict:
        pass
    
    @classmethod
    def get_futures_crypto_info(self) -> list[Asset]:
        pass