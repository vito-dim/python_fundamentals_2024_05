from math import ceil

budget = float(input())
students_count = int(input())
price_pack_of_flour = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

free_flour_packs = students_count // 5
total_flour_price = price_pack_of_flour * (students_count - free_flour_packs)
total_egg_price = price_single_egg * 10 * students_count
total_apron_price = price_single_apron * (ceil(students_count * (1 + 0.20)))

total_cost = total_flour_price + total_egg_price + total_apron_price

if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    money_needed = total_cost - budget
    print(f"{money_needed:.2f}$ more needed.")
