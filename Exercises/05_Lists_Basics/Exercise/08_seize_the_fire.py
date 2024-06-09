list_of_fires_to_put_out = input().split('#')
water_amount = int(input())
water_left = water_amount

high_range = range(81, 125 + 1)
medium_range = range(51, 80 + 1)
low_range = range(1, 50 + 1)

successful_put_out_cells = ['Cells:']
effort = 0
total_fire = 0

for current_fire_index in range(len(list_of_fires_to_put_out)):
    current_fire_information = list_of_fires_to_put_out[current_fire_index].split(' = ')
    current_fire_type = current_fire_information[0]
    current_cell_value = int(current_fire_information[1])
    current_fire_range = 0

    if current_fire_type == 'High':
        current_fire_range = high_range
    elif current_fire_type == 'Medium':
        current_fire_range = medium_range
    elif current_fire_type == 'Low':
        current_fire_range = low_range

    if current_cell_value in current_fire_range and water_left >= current_cell_value:
        water_left -= current_cell_value
        successful_put_out_cells.append(f' - {current_cell_value}')
        effort += 0.25 * current_cell_value
        total_fire += current_cell_value

for cell in successful_put_out_cells:
    print(cell)

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

# # Modify initial string by replacing '#' with ' = '
# for index in range(len(information_about_fire)):
#     if information_about_fire[index] == '#':
#         information_about_fire = information_about_fire.replace('#', ' = ')

