from decimal import Decimal
from typing import Optional


class Product:
    def __init__(
        self, name: str, unit_price: Decimal, category: Optional[str] = None
    ):
        self.name = name
        self.unit_price = unit_price
        self.category = category or ""
