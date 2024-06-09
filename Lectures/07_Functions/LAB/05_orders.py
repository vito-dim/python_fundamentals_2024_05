def order_price(order_item: str, quantity: int) -> float:
    """
    :param order_item: (str) ordered item ->  "coffee", "coke", "water", or "snacks"
    :param quantity: (int) count of ordered items
    :return: (float) the price of the ordered item, depending on its type
    """
    item_price = None
    if order_item == 'coffee':
        item_price = 1.50
    elif order_item == 'coke':
        item_price = 1.40
    elif order_item == 'water':
        item_price = 1.00
    elif order_item == 'snacks':
        item_price = 2.00
    return item_price * quantity


ordered_item = input()
item_quantity = int(input())
ordered_items_price = order_price(ordered_item, item_quantity)
print(f'{ordered_items_price:.2f}')
