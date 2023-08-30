# Python
from pprint import pprint

# Project
from crypto_info.models.asset import Asset
from crypto_info.abstracts.exchange import Exchange
from crypto_info.services.asset_service import AssetService

# Externals
from decouple import config
import requests as r


class Binance(Exchange):
    def __init__(self, asset_service: AssetService):
        self._base_url = "https://fapi.binance.com"
        self._exchange_info_endpoint = "/fapi/v1/exchangeInfo"
    
    
    def get_futures_exchange_info(self, symbol:str=None) -> dict:
        url = self._base_url + self._exchange_info_endpoint
        
        try:
            response = r.get(url, params=params)
            if response.status_code in range(200, 300):
                return response.json()
            response.raise_for_status()
            
        except r.exceptions.ConnectionError as e:
            print(f"Connection Error:\n{e}")
            
        except r.exceptions.RequestException as e:
            print(f"Request Exception\n{e}")
    
    
    async def _filter_symbols_from_exchange_info(self, info: dict) -> list[dict]:
        s = list(filter(lambda d: d["symbol"][-4:].lower() == "usdt", info))
        return s
    
    
    async def _create_assets(self, data: list[dict]) -> list[Asset]:
        tasks = []
        for d in data:
            symbol = d["symbol"].lower()
            
            a = Asset(
                symbol=symbol, tick_size="", step_size="", min_qty="", min_cost=""
            )
    
    
    async def _get_futures_symbol_info_from_exchange_info(self) -> list[Asset]:
        info = self.get_futures_exchange_info()
        symbols = await self._filter_symbols_from_exchange_info(info["symbols"])
        assets = await self._create_assets(symbols)
        return True
