# activation_key = input()
#
# command = input()
# while command != "Generate":
#     current_command = command.split(">>>")
#     if current_command[0] == "Contains":
#         substring = current_command[1]
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif current_command[0] == "Flip":
#         mode = current_command[1].lower()  # lower or upper
#         start_index = int(current_command[2])
#         end_index = int(current_command[3])
#         text_to_flip = activation_key[start_index:end_index]
#         if mode == "upper":
#             activation_key = activation_key.replace(text_to_flip, text_to_flip.upper())
#         else:
#             activation_key = activation_key.replace(text_to_flip, text_to_flip.lower())
#         print(activation_key)
#
#     elif current_command[0] == "Slice":
#         start_index = int(current_command[1])
#         end_index = int(current_command[2])
#         text_to_delete = activation_key[start_index:end_index]
#         activation_key = activation_key.replace(text_to_delete, '')
#         print(activation_key)
#
#     command = input()
#
# print(f"Your activation key is: {activation_key}")
def contains(raw_key: str, cmd_details: list):
    substring = cmd_details[1]
    if substring in raw_key:
        return f"{raw_key} contains {substring}"
    return "Substring not found!"


def flip(raw_key: str, cmd_details: list):
    upper_lower = cmd_details[1]
    start_index = int(cmd_details[2])
    end_index = int(cmd_details[3])
    left_part = raw_key[:start_index]
    right_part = raw_key[end_index:]
    string_to_manipulate = raw_key[start_index:end_index]
    if upper_lower.lower() == "upper":
        string_to_manipulate = raw_key[start_index:end_index].upper()
        raw_key = left_part + string_to_manipulate + right_part

    elif upper_lower.lower() == "lower":
        string_to_manipulate = raw_key[start_index:end_index].lower()
        raw_key = left_part + string_to_manipulate + right_part

    return raw_key


def slice_cmd(raw_key: str, cmd_details: list):
    start_index = int(cmd_details[1])
    end_index = int(cmd_details[2])
    raw_key = raw_key[:start_index] + raw_key[end_index:]
    return raw_key


raw_activation_key = input()

command = input()
while command != 'Generate':
    command_details = command.split('>>>')
    current_command = command_details[0]

    if "Contains" == current_command:
        print(contains(raw_activation_key, command_details))

    elif "Flip" == current_command:
        raw_activation_key = flip(raw_activation_key, command_details)
        print(raw_activation_key)

    elif "Slice" == current_command:
        raw_activation_key = slice_cmd(raw_activation_key, command_details)
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")
