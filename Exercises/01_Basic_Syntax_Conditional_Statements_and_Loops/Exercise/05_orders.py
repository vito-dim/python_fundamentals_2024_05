order_count = int(input())

total_price = 0

for _ in range(order_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if not 0.01 <= price_per_capsule <= 100.00:     # if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if days not in range(1, 31 + 1):
        continue
    if capsules_needed not in range(1, 2000 + 1):
        continue

    current_price = price_per_capsule * days * capsules_needed
    total_price += current_price

    print(f'The price for the coffee is: ${current_price:.2f}')

print(f'Total: ${total_price:.2f}')
