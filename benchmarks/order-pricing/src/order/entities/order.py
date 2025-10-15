from decimal import Decimal
from typing import List
from .order_item import OrderItem


class Order:
    def __init__(self):
        self.total_amount: Decimal = Decimal("0")
        self.original_amount: Decimal = Decimal("0")
        self.discount: Decimal = Decimal("0")
        self.items: List[OrderItem] = []

    def add_item(self, item: OrderItem):
        self.items.append(item)
