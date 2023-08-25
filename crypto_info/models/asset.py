# Python
from dataclasses import field
from dataclasses import dataclass
# Project
# Externals

@dataclass(kw_only=True)
class Asset:
    symbol: str
    tick_size: str
    step_size: str
    min_qty: str
    min_cost: str
    max_leverage: str = field(default=None, init=False)
    price_precision: int = field(default=None, init=False)
    qty_precision: int = field(default=None, init=False)
    price_factor: int = field(default=None, init=False)
    qty_factor: int = field(default=None, init=False)
    
    