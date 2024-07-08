list_of_integers = [int(digit) for digit in input().split('|')]

grid_list = list_of_integers.copy()
items_collected = 0

command = input()
while command != 'Adventure over':

    if 'Step' in command:
        step_type, start_index, steps = command.split('$')
        current_index = 0
        if int(start_index) not in range(len(grid_list)):
            command = input()
            continue

        if 'Backward' in step_type:
            current_index = (int(start_index) - int(steps)) % len(grid_list)
        elif 'Forward' in step_type:
            current_index = (int(start_index) + int(steps)) % len(grid_list)

        items_collected += grid_list[current_index]
        grid_list[current_index] = 0

    elif 'Double' in command:
        current_index = int(command.split()[1])
        if current_index in range(len(grid_list)):
            grid_list[current_index] *= 2

    elif command == 'Switch':
        grid_list = grid_list[::-1]

    command = input()

grid_list_as_string = [str(item) for item in grid_list]
print(' - '.join(grid_list_as_string))
print(f'Robo finished the adventure with {items_collected} items!')
