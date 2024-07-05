#1
characters = [character for character in input() if character != " "]
letters = {}
for character in characters:
    if character not in letters.keys(): #if character not in letters
        letters[character] = 0
    letters[character] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")


#2
resources = {}
while True:
    current_resources = input()
    if current_resources == "stop":
        break
    current_quantity = int(input())
    if current_resources not in resources.keys():
        resources[current_resources] = 0
    resources[current_resources] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

#3

countries = input().split(", ")
capitals = input().split(", ")
# final_dictionary = {countries[index]:capitals[index] for index in range(len(countries))}
final_dictionary = dict(zip(countries, capitals))
for country, capital in final_dictionary.items():
    print(f"{country} -> {capital}")

#4
phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number
searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

#5
materials = {"shards": 0, "fragments": 0, "motes": 0}
won_legendary_item = False
while not won_legendary_item:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index+1].lower()
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print("Shadowmourne obtained!")
            won_legendary_item = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            won_legendary_item = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            won_legendary_item = True
        if won_legendary_item:
            break
for material, quantity in materials.items():
    print(f"{material}: {quantity}")

#7
parking = {}
number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    if current_command[0] == "register":
        username, license_plate_number = current_command[1], current_command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif current_command[0] == "unregister":  # else
        username = current_command[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")


#11
force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_is_part_of_the_force = False
        for list_of_force_users in force_side_dictionary.values():
            if force_user in list_of_force_users:
                force_user_is_part_of_the_force = True
                break
        if not force_user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif "->" in command:  # else:
        force_user, force_side = command.split(" -> ")
        for list_of_force_users in force_side_dictionary.values():
            if force_user in list_of_force_users:
                list_of_force_users.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, list_of_force_users in force_side_dictionary.items():
    if list_of_force_users: #if len(list_of_force_users) > 0
        print(f"Side: {force_side}, Members: {len(list_of_force_users)}")
        for force_user in list_of_force_users:
            print(f"! {force_user}")



#12

users_points_dictionary = {}
courses_dictionary = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break
    elif len(current_result) == 2: # Someone is banned
        name = current_result[0]
        del users_points_dictionary[name]
    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in users_points_dictionary.keys():
            users_points_dictionary[name] = 0
        if users_points_dictionary[name] < points:
            users_points_dictionary[name] = points
        if course not in courses_dictionary.keys():
            courses_dictionary[course] = 0
        courses_dictionary[course] += 1
print("Results:")
for name, max_points in users_points_dictionary.items():
    print(f"{name} | {max_points}")
print("Submissions:")
for course, number_of_students in courses_dictionary.items():
    print(f"{course} - {number_of_students}")
