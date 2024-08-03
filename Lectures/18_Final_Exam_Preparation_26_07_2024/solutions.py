# 01 secret_chat

def insert_space(message, index):
    return message[:index] + ' ' + message[index:]


def reverse_substring(message, substring):
    if substring in message:
        message = message.replace(substring, '', 1)
        reversed_substring = substring[::-1]
        return message + reversed_substring
    else:
        return 'error'


def change_all(message, substring, replacement):
    return message.replace(substring, replacement)


def process_commands(message, commands):
    for command in commands:
        parts = command.split(':|:')
        action = parts[0]

        if action == 'InsertSpace':
            index = int(parts[1])
            message = insert_space(message, index)

        elif action == 'Reverse':
            substring = parts[1]
            result = reverse_substring(message, substring)
            if result == 'error':
                print('error')
                continue
            else:
                message = result
        elif action == 'ChangeAll':
            substring = parts[1]
            replacement = parts[2]
            message = change_all(message, substring, replacement)

        print(message)

    return message


secret_message = input()
all_commands = []

while True:
    command = input()
    if command == 'Reveal':
        break
    all_commands.append(command)

decrypt_message = process_commands(secret_message, all_commands)
print(f'You have a new text message: {decrypt_message}')


# 02_destination_mapper
import re

map_string = input()

pattern = r'(=|\/)([A-Z][a-zA-Z]{2,})\1'

matches = re.findall(pattern, map_string)

destinations = [match[1] for match in matches]

travel_points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {travel_points}")



# 03_the_pianist
n = int(input())

collection = {}

for _ in range(n):
    piece_info = input().split('|')
    piece = piece_info[0]
    composer = piece_info[1]
    key = piece_info[2]
    collection[piece] = {'composer': composer, 'key': key}

while True:
    command = input()

    if command == 'Stop':
        break

    command_parts = command.split('|')
    current_action = command_parts[0]

    if current_action == 'Add':
        piece = command_parts[1]
        composer = command_parts[2]
        key = command_parts[3]

        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_action == 'Remove':
        piece = command_parts[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_action == 'ChangeKey':
        piece = command_parts[1]
        new_key = command_parts[2]
        if piece in collection:
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
    
# 04_ad_astra
import re

data = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

matches = re.finditer(pattern, data)

calories_counter = 0
food_items = []

for match in matches:
    item = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))

    calories_counter += calories
    food_items.append([item, expiration_date, calories])


days = calories_counter // 2000

print(f"You have food to last you for: {days} days!")

for item, expiration_date, calories in food_items:
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")