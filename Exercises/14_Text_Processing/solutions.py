#1
 
def length_is_valid(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False
 
 
def characters_are_valid(some_username):
    for character in some_username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True
 
 
def no_redundant_symbols(some_username):
    if " " in some_username:
        return False
    return True
 
def username_is_valid(some_username):
    if length_is_valid(some_username) and \
            characters_are_valid(some_username) and \
            no_redundant_symbols(some_username):
        return True
    return False
 
 
usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
 
 
#2
first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else: # len(first_string) == len(second_string)
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)
 
 
#3
 
file_path = input().split("\\")
filename, extension = file_path[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
 
 
#4
 
initial_text = input()
encrypted_version = ""
for character in initial_text:
    encrypted_character = chr(ord(character) + 3)
    encrypted_version += encrypted_character
print(encrypted_version)
 
#5
single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ':':
        print(f":{single_string[index+1]}")
 
 
 
#6
 
some_string = input()
final_string = ""
last_added_character = ""
for current_character in some_string:
    if current_character != last_added_character:
        final_string += current_character
        last_added_character = current_character
print(final_string)
 
#7
some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # Explosion mark
    elif some_string[index] == ">":
        final_string += ">" # some_string[index]
        strength += int(some_string[index+1])
    # No explosion, no explosion mark
    else:
        final_string += some_string[index]
print(final_string)
 
 
#8
 
all_strings = input().split()
total_sum = 0
for current_string in all_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    current_number = int(current_string[1:len(current_string) - 1])
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position
print(f"{total_sum:.2f}")
 
#9
 
text = input()
final_message = ""
sub_string = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        sub_string += text[index].upper()
    else:
        for next_characters in range(index, len(text)):
            if not text[next_characters].isdigit():
                break
            repetitions += text[next_characters]
        final_message += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)
 
 
#10
 
 
def checking_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbols:
        for uninterrupted_winning_symbol_length in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbol * uninterrupted_winning_symbol_length
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if uninterrupted_winning_symbol_length == 10: # We have Jackpot
                    return f'ticket "{ticket}" - {uninterrupted_winning_symbol_length}{current_winning_symbol} Jackpot!'
                # We have winning ticket (no Jackpot)
                return f'ticket "{ticket}" - {uninterrupted_winning_symbol_length}{current_winning_symbol}'
    return f'ticket "{ticket}" - no match'
 
 
 
tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(checking_ticket(current_ticket))