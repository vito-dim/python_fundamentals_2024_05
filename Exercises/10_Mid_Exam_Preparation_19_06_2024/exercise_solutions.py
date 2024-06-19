#1
first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
number_of_students = int(input())
total_efficiency_per_hour = first_employee_per_hour \
                            + second_employee_per_hour \
                            + third_employee_per_hour
total_time = 0
while number_of_students > 0:
    total_time += 1
    if total_time % 4 == 0:
        continue
    number_of_students -= total_efficiency_per_hour
print(f"Time needed: {total_time}h.")
 
#1.1
 
first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
number_of_students = int(input())
total_efficiency_per_hour = first_employee_per_hour \
                            + second_employee_per_hour \
                            + third_employee_per_hour
total_time = 0
hours_counter = 0
while number_of_students > 0:
    hours_counter += 1
    if hours_counter % 4 == 0:
        total_time += 1
        continue
    number_of_students -= total_efficiency_per_hour
    total_time += 1
print(f"Time needed: {total_time}h.")
 
#2
def loot(current_treasure_chest: list, items: list) -> list:
    for item in items:
        if item not in current_treasure_chest:
            current_treasure_chest.insert(0, item)
    return current_treasure_chest
 
 
def drop(current_treasure_chest, current_index):
    if current_index in range(len(current_treasure_chest)):
        current_treasure_chest.append(current_treasure_chest.pop(current_index))
    return current_treasure_chest
 
 
def steal(current_treasure_chest, current_steal_count):
    if current_steal_count >= len(current_treasure_chest):
        print(", ".join(current_treasure_chest))
        return []
    steal_index = len(current_treasure_chest) - current_steal_count
    print(", ".join(current_treasure_chest[steal_index:]))
    current_treasure_chest = current_treasure_chest[:steal_index]
    return current_treasure_chest
 
 
treasure_chest = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        treasure_chest = loot(treasure_chest, command[1:])
    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif action == "Steal":  # else
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
    command = input().split()
if not treasure_chest: # if treasure_chest == 0
    print("Failed treasure hunt.")
else:
    average = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
 
 
#2.1 
 
treasure_chest = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    action = command[0]
    if action == "Loot":
        items = command[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif action == "Drop":
        index = int(command[1])
        if index in range(len(treasure_chest)):
            treasure_chest.append(treasure_chest.pop(index))
    elif action == "Steal":  # else
        count = int(command[1])
        if count >= len(treasure_chest):
            print(", ".join(treasure_chest))
            treasure_chest = []
        else:
            steal_index = len(treasure_chest) - count
            print(", ".join(treasure_chest[steal_index:]))
            treasure_chest = treasure_chest[:steal_index]
    command = input().split()
if not treasure_chest:  # if treasure_chest == 0
    print("Failed treasure hunt.")
else:
    average = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
 
#3
 
sequence_of_targets = [int(target) for target in input().split()]
command = input().split()
while command[0] != "End":
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets[index] -= value
            if sequence_of_targets[index] <= 0:
                del sequence_of_targets[index]
    elif action == "Add":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":  # else:
        if index - value not in range(len(sequence_of_targets)) or \
                index + value not in range(len(sequence_of_targets)):
            print("Strike missed!")
        else:
            before_strike = sequence_of_targets[:index - value]
            after_strike = sequence_of_targets[index + value + 1:]
            sequence_of_targets = before_strike + after_strike
    command = input().split()
print(*sequence_of_targets, sep="|")
