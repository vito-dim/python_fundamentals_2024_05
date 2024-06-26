list_of_integers = [int(digit) for digit in input().split('|')]

grid_list = list_of_integers.copy()
items_collected = 0

command = input()
while command != 'Adventure over':

    if 'Step Backward' in command:
        command_attributes = command.split('$')
        start_index = int(command_attributes[1])
        steps = int(command_attributes[2])

        if start_index in range(len(grid_list)):
            grid_value = 0
            grid_index = 0

            while True:
                if steps == 0:
                    break

                for index in range(len(grid_list) - 1, start_index - 1, -1):
                    if steps == 0:
                        break
                    steps -= 1
                    grid_value = grid_list[index]
                    grid_index = index

            items_collected += grid_value
            grid_list[grid_index] = 0

    elif 'Step Forward' in command:
        command_attributes = command.split('$')
        start_index = int(command_attributes[1])
        steps = int(command_attributes[2])

        if start_index in range(len(grid_list)):
            grid_value = 0
            grid_index = 0

            while True:
                if steps == 0:
                    break

                for index in range(start_index, len(grid_list)):
                    if steps == 0:
                        break
                    steps -= 1
                    grid_value = grid_list[index]
                    grid_index = index

            items_collected += grid_value
            grid_list[grid_index] = 0

    elif 'Double ' in command:
        current_index = int(command.split()[1])
        if current_index in range(len(grid_list)):
            grid_list[current_index] *= 2

    elif command == 'Switch':
        grid_list = grid_list[::-1]

    command = input()

grid_list_as_string = [str(item) for item in grid_list]
print(' - '.join(grid_list_as_string))
print(f'Robo finished the adventure with {items_collected} items!')
