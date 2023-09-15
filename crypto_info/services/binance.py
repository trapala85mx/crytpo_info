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
        super().__init__(asset_service=asset_service)
        self._name = "BINANCE"
        self._base_url = "https://fapi.binance.com"
    
    
    def futures_exchange_info(self) -> dict:
        """Gets the exchange info from Binance API

        Returns:
            dict: Dictionary with Exchange Information
        """
        EXCHANGE_INFO_ENDPOINT = "/fapi/v1/exchangeInfo"
        url = self._base_url + EXCHANGE_INFO_ENDPOINT
        
        try:
            response = r.get(url)
            if response.status_code in range(200, 300):
                return response.json()
            response.raise_for_status()
            
        except r.exceptions.ConnectionError as e:
            print(f"Connection Error:\n{e}")
            
        except r.exceptions.RequestException as e:
            print(f"Request Exception\n{e}")
        
        except Exception as e:
            print(f"Error while getting Exchange Info for {self._name}")
    
    
    def get_24hr_change_statistics(self, symbol:str =None) -> dict | list[dict]:
        """Gets the last 24 hr statistics

        Args:
            symbol (str, optional): Symbol to get statistics. Defaults to None to retrieve all
                                    symbols statistics

        Returns:
            dict | list[dict]: a dict if symbol is sent else returns a list where each dict is a
                                symbol data
        """        
        STATISTICS_24HR = "/fapi/v1/ticker/24hr"
        url = self._base_url + STATISTICS_24HR
        params = None
        
        if not symbol is None:
            params = {
                'symbol': symbol.lower()
            }
            
        try:
            response = r.get(url, params=params)
            if response.status_code in range(200, 300):
                return response.json()
            
            response.raise_for_status()
        
        except r.exceptions.ConnectionError as e:
            print(f"Connection Error while getting 24 hr statistics\n{e}")
        
        except r.exceptions.RequestException as e:
            print(f'Request Exception\n{e}')
    
    
    async def save_assets_info(self) -> bool:
        """Save the data for all crypto into DataBase

        Returns:
            bool: True if Data is Saved False if Not
        """        
        exchange_info = self.futures_exchange_info()
        symbols = self._filter_symbols_from_exchange_info(exchange_info['symbols'])
        assets = await self._create_assets(symbols)
        return self._asset_service.insert_many_assets(assets)
    
    
    def _filter_symbols_from_exchange_info(self, symbols: dict) -> list[dict]:
        """Filter symbols from Echange Information. Just the ones with USDT at the end are
            considered

        Args:
            symbols (dict[dict]): Dictionary that has all symbols info in a dictionary

        Returns:
            list[dict]: List that has the Dictionary for evey symbol filtered
        """        
        symbols_list = list(filter(lambda d: d["symbol"][-4:].lower() == "usdt", symbols))
        return symbols_list
    
    
    async def _create_assets(self, symbols: list[dict]) -> list[Asset]:
        """Creates an Asset object for every symbol filtered

        Args:
            symbols (list[dict]): List of every symbol dict filtered

        Returns:
            list[Asset]: List of all Assets created
        """        
        assets = []
        for d in symbols:
            symbol = d['symbol'].lower()
            
            for filter in d['filters']:
                if filter['filterType'] == 'PRICE_FILTER':
                    priceFilter_minPrice = filter['minPrice']
                    priceFilter_maxPrice = filter['maxPrice']
                    priceFilter_tickSize = filter['tickSize']
                
                if filter['filterType'] == 'LOT_SIZE':
                    lotSizeFilter_maxQty = filter['maxQty']
                    lotSizeFilter_minQty = filter['minQty']
                    lotSizeFilter_stepSize = filter['stepSize']
            
                if filter['filterType'] == 'MARKET_LOT_SIZE':
                    marketLotSizeFilter_maxQty = filter['maxQty']
                    marketLotSizeFilter_minQty = filter['minQty']
                    marketLotSizeFilter_stepSize = filter['stepSize']
            
                if filter['filterType'] == 'MIN_NOTIONAL':
                    minNotionalFilter_notional = filter['notional']
                
                if filter['filterType'] == 'PERCENT_PRICE':
                    percentPriceFilter_multiplierUp = filter['multiplierUp']
                    percentPriceFilter_multiplierDown = filter['multiplierDown']
                    percentPriceFilter_multiplierDecimal = filter['multiplierDecimal']
                
            a = Asset(
                    symbol=symbol,
                    priceFilter_maxPrice=priceFilter_maxPrice,
                    priceFilter_minPrice=priceFilter_minPrice,
                    priceFilter_tickSize=priceFilter_tickSize,
                    lotSizeFilter_maxQty=lotSizeFilter_maxQty,
                    lotSizeFilter_minQty=lotSizeFilter_minQty,
                    lotSizeFilter_stepSize=lotSizeFilter_stepSize,
                    marketLotSizeFilter_maxQty=marketLotSizeFilter_maxQty,
                    marketLotSizeFilter_minQty=marketLotSizeFilter_minQty,
                    marketLotSizeFilter_stepSize=marketLotSizeFilter_stepSize,
                    minNotionalFilter_notional=minNotionalFilter_notional,
                    percentPriceFilter_multiplierUp=percentPriceFilter_multiplierUp,
                    percentPriceFilter_multiplierDown=percentPriceFilter_multiplierDown,
                    percentPriceFilter_multiplierDecimal=percentPriceFilter_multiplierDecimal
                )
            self._asset_service.set_attributes(a)
            
            assets.append(a)
        return assets