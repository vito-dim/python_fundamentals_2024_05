bakery = {}

command = input()
while command != 'statistics':
    product, quantity = command.split(': ')
    if product in bakery:
        bakery[product] += int(quantity)
    else:
        bakery[product] = int(quantity)

    command = input()

count_all_products = len(bakery.keys())
sum_all_quantities = sum(bakery.values())

print("Products in stock:")
for product, quantity in bakery.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
