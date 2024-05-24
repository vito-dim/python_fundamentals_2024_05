# recipe - eggs = 1 pack, flour = 1kg, milk = 0.250 l
budget = float(input())
flour_price = float(input())  # flour per kg
eggs_pack_price = 0.75 * flour_price
milk_price = (1 + 0.25) * flour_price  # milk per liter
loaf_price = eggs_pack_price + flour_price + 0.250 * milk_price

budget_left = budget
loaf_count = 0
eggs_count = 0

while budget_left > loaf_price:
    loaf_count += 1
    eggs_count += 3
    budget_left -= loaf_price

    if loaf_count % 3 == 0:
        eggs_count -= (loaf_count - 2)

print(f'You made {loaf_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget_left:.2f}BGN left.')
