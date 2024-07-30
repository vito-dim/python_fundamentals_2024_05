resources = {}

command = input()
while command != 'stop':
    current_resource = command
    current_quantity = int(input())

    if current_resource not in resources:
        resources[current_resource] = current_quantity
    else:
        resources[current_resource] += current_quantity

    command = input()

for item, count in resources.items():
    print(f'{item} -> {count}')
