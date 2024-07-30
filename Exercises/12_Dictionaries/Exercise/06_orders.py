products = {}

command = input()
while command != 'buy':
    product_name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product_name not in products:
        products[product_name] = {'price': price, 'quantity': quantity}
    else:
        products[product_name]['quantity'] += quantity
        products[product_name]['price'] = price

    command = input()

for product in products:
    total_price = products[product]['price'] * products[product]['quantity']
    print(f"{product} -> {total_price:.2f}")
