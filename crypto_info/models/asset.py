# Python
from dataclasses import field
from dataclasses import dataclass
# Project
# Externals

@dataclass(kw_only=True)
class Asset:
    """Class to represent an Asset in the proyect
    """    
    symbol: str
    priceFilter_minPrice : str
    priceFilter_maxPrice : str
    priceFilter_tickSize : str
    lotSizeFilter_minQty : str
    lotSizeFilter_maxQty : str
    lotSizeFilter_stepSize : str
    marketLotSizeFilter_minQty : str
    marketLotSizeFilter_maxQty : str
    marketLotSizeFilter_stepSize : str
    minNotionalFilter_notional : str
    percentPriceFilter_multiplierUp : str
    percentPriceFilter_multiplierDown : str
    percentPriceFilter_multiplierDecimal : str
    price_precision : int = field(default=None, init=False)
    qty_precision : int = field(default=None, init=False)
    price_factor : int = field(default=None, init=False)
    qty_factor : int = field(default=None, init=False)
    
    
    def __str__(self) -> str:
        return f"symbol:{self.symbol.upper()}"
    
    
    