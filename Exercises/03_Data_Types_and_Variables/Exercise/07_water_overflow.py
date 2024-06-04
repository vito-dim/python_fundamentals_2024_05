number_of_iterations = int(input())
tank_capacity = 255
total_poured_water = 0

for _ in range(number_of_iterations):
    current_poured_water = int(input())
    total_poured_water += current_poured_water

    if total_poured_water > tank_capacity:
        print('Insufficient capacity!')
        total_poured_water -= current_poured_water

print(total_poured_water)


# number_of_lines = int(input())
# tank_capacity = 255
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:  # no enough capacity for current water
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
# print(255 - tank_capacity)
