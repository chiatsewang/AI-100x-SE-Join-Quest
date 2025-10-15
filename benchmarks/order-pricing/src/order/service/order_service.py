from typing import List
from decimal import Decimal
from order.entities.order import Order
from order.entities.order_item import OrderItem


class OrderService:
    def __init__(
        self,
        threshold_discount=None,
        bogo_cosmetics=False,
        double_eleven=False,
    ):
        self.threshold_discount = threshold_discount
        self.bogo_cosmetics = bogo_cosmetics
        self.double_eleven = double_eleven

    def checkout(self, items: List[OrderItem]) -> Order:
        """
        Process order checkout with promotions applied.

        Args:
            items: List of order items

        Returns:
            Order with calculated amounts and items
        """
        order = Order()

        # Calculate original amount and add items to order
        original_amount = self._calculate_original_amount(items, order)
        order.original_amount = original_amount

        # Apply promotions
        double_eleven_discount = self._apply_double_eleven_discount(items)
        threshold_discount = self._apply_threshold_discount(original_amount)
        total_discount = double_eleven_discount + threshold_discount

        order.discount = total_discount
        order.total_amount = original_amount - total_discount

        return order

    def _calculate_original_amount(
        self, items: List[OrderItem], order: Order
    ) -> Decimal:
        """
        Calculate original amount and add items to order with promotions applied
        """
        original_amount = Decimal("0")

        for item in items:
            # Calculate item subtotal (based on purchased quantity only)
            item_total = item.product.unit_price * item.quantity
            original_amount += item_total

            # Determine final quantity after applying promotions
            final_quantity = self._apply_bogo_promotion(item)

            # Add item with final quantity to order
            order_item = OrderItem(item.product, final_quantity)
            order.add_item(order_item)

        return original_amount

    def _apply_bogo_promotion(self, item: OrderItem) -> int:
        """
        Apply buy-one-get-one promotion if applicable.

        BOGO logic: For each item purchased, add 1 free item per purchase transaction.
        - Buy 1 -> Get 2 (1 purchased + 1 free)
        - Buy 2 -> Get 3 (2 purchased + 1 free for the transaction)
        """
        if self.bogo_cosmetics and item.product.category == "cosmetics":
            # Buy one get one: add 1 free item per product type
            return item.quantity + 1
        return item.quantity

    def _apply_threshold_discount(self, original_amount: Decimal) -> Decimal:
        """Apply threshold discount if configured and threshold is met"""
        if not self.threshold_discount:
            return Decimal("0")

        threshold = self.threshold_discount["threshold"]
        discount_amount = self.threshold_discount["discount"]

        if original_amount >= threshold:
            return discount_amount

        return Decimal("0")

    def _apply_double_eleven_discount(self, items: List[OrderItem]) -> Decimal:
        """
        Apply Double Eleven bulk purchase discount.

        For every 10 items of the same product, apply 20% discount to those 10 items.
        Example: Buy 12 items at 100 each = (10*100*0.8) + (2*100) = 800 + 200 = 1000
                 Discount = 10*100*0.2 = 200
        """
        if not self.double_eleven:
            return Decimal("0")

        total_discount = Decimal("0")

        for item in items:
            # Calculate how many complete sets of 10 items
            sets_of_ten = item.quantity // 10

            if sets_of_ten > 0:
                # Each set of 10 gets 20% discount
                discount_per_set = (
                    item.product.unit_price * 10 * Decimal("0.2")
                )
                item_discount = discount_per_set * sets_of_ten
                total_discount += item_discount

        return total_discount
