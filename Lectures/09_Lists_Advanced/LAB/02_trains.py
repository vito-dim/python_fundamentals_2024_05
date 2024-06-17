number_of_wagons = int(input())
train = [0] * number_of_wagons

command = input()
while command != 'End':
    current_command_attributes = command.split()
    for current_command in command:
        current_command_attributes.append(current_command)

    if 'add'.lower() in current_command_attributes:
        people = int(current_command_attributes[1])
        train[-1] += people
    elif 'insert'.lower() in current_command_attributes:
        people = int(current_command_attributes[2])
        current_wagon_number = int(current_command_attributes[1])
        train[current_wagon_number] += people

    elif 'leave'.lower() in current_command_attributes:
        people = int(current_command_attributes[2])
        current_wagon_number = int(current_command_attributes[1])
        train[current_wagon_number] -= people

    command = input()

print(train)
