decoration_quantity = int(input())
days_left = int(input())

ornament_set_price = 2
ornament_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17

money_needed = 0
spirit_gained = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decoration_quantity += 2

    if day % 2 == 0:
        money_needed += (ornament_set_price * decoration_quantity)
        spirit_gained += ornament_points

    if day % 3 == 0:
        money_needed += (tree_skirt_price * decoration_quantity) + (tree_garland_price * decoration_quantity)
        spirit_gained += tree_skirt_points + tree_garland_points

    if day % 5 == 0:
        money_needed += (tree_lights_price * decoration_quantity)
        spirit_gained += tree_lights_points
        if day % 3 == 0:
            spirit_gained += 30

    if day % 10 == 0:
        spirit_gained -= 20
        money_needed += (tree_lights_price + tree_garland_price + tree_skirt_price)

    if day == days_left and day % 10 == 0:
        spirit_gained -= 30

print(f'Total cost: {money_needed}')
print(f'Total spirit: {spirit_gained}')
