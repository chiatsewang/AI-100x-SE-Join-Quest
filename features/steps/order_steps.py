from behave import given, when, then
from decimal import Decimal
from order.entities.product import Product
from order.entities.order_item import OrderItem
from order.service.order_service import OrderService


@given("no promotions are applied")
def step_no_promotions(context):
    """No promotions are configured"""
    # No action needed for now
    pass


@given("the threshold discount promotion is configured:")
def step_configure_threshold_discount(context):
    """Configure threshold discount promotion"""
    # Store threshold discount configuration in context
    row = context.table[0]
    context.threshold_discount = {
        "threshold": Decimal(row["threshold"]),
        "discount": Decimal(row["discount"]),
    }


@given("the buy one get one promotion for cosmetics is active")
def step_activate_bogo_cosmetics(context):
    """Activate buy-one-get-one promotion for cosmetics"""
    context.bogo_cosmetics = True


@when("a customer places an order with:")
def step_place_order(context):
    """Place an order with the given items"""
    context.order_items = []

    # Create OrderService with promotions if configured
    threshold_discount = getattr(context, "threshold_discount", None)
    bogo_cosmetics = getattr(context, "bogo_cosmetics", False)
    context.order_service = OrderService(
        threshold_discount=threshold_discount, bogo_cosmetics=bogo_cosmetics
    )

    for row in context.table:
        product_name = row["productName"]
        quantity = int(row["quantity"])
        unit_price = Decimal(row["unitPrice"])
        category = row.get("category", "")

        product = Product(product_name, unit_price, category)
        order_item = OrderItem(product, quantity)
        context.order_items.append(order_item)

    context.result_order = context.order_service.checkout(context.order_items)


@then("the order summary should be:")
def step_verify_order_summary(context):
    """Verify the order summary amounts"""
    expected = context.table[0]

    if "totalAmount" in expected.headings:
        expected_total = Decimal(expected["totalAmount"])
        assert (
            context.result_order.total_amount == expected_total
        ), f"Expected total amount {expected_total}, but got {context.result_order.total_amount}"

    if "originalAmount" in expected.headings:
        expected_original = Decimal(expected["originalAmount"])
        assert (
            context.result_order.original_amount == expected_original
        ), f"Expected original amount {expected_original}, but got {context.result_order.original_amount}"

    if "discount" in expected.headings:
        expected_discount = Decimal(expected["discount"])
        assert (
            context.result_order.discount == expected_discount
        ), f"Expected discount {expected_discount}, but got {context.result_order.discount}"


@then("the customer should receive:")
def step_verify_received_items(context):
    """Verify the items customer will receive"""
    expected_items = list(context.table)
    actual_items = context.result_order.items

    assert len(expected_items) == len(
        actual_items
    ), f"Expected {len(expected_items)} items, but got {len(actual_items)}"

    for i, expected_row in enumerate(expected_items):
        expected_name = expected_row["productName"]
        expected_quantity = int(expected_row["quantity"])

        actual_item = actual_items[i]
        actual_name = actual_item.product.name
        actual_quantity = actual_item.quantity

        assert (
            expected_name == actual_name
        ), f"Expected product '{expected_name}', but got '{actual_name}'"
        assert (
            expected_quantity == actual_quantity
        ), f"Expected quantity {expected_quantity}, but got {actual_quantity}"
