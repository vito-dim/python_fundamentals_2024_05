# text = input()
#
# command = input().split()
# while "Done" not in command:
#     if "Change" == command[0]:
#         char_to_replace = command[1]
#         replacement_char = command[2]
#         text = text.replace(char_to_replace, replacement_char)
#         print(text)
#
#     elif "Includes" == command[0]:
#         sub_string = command[1]
#         check_if_included = sub_string in text
#         print(check_if_included)
#
#     elif "End" == command[0]:
#         sub_string = command[1]
#         check_if_endswith = text.endswith(sub_string)
#         print(check_if_endswith)
#
#     elif "Uppercase" == command[0]:
#         text = text.upper()
#         print(text)
#
#     elif "FindIndex" == command[0]:
#         char_to_find = command[1]
#         index_found = text.index(char_to_find)
#         print(index_found)
#
#     elif "Cut" == command[0]:
#         start_index = int(command[1])
#         count = int(command[2])
#         left_part = text[start_index:]
#         part_to_remove = left_part[count:]
#         cut_result = left_part.replace(part_to_remove, "")
#         print(cut_result)
#
#     command = input().split()
def change_string(full_command: list, string: str) -> str:
    char_to_replace = full_command[1]
    replacement_char = full_command[2]
    string = string.replace(char_to_replace, replacement_char)
    return string


def includes_check(full_command: list, string: str) -> bool:
    sub_string = full_command[1]
    if sub_string in string:
        return True
    return False


def ends_check(full_command: list, string: str):
    sub_string = full_command[1]
    if string.endswith(sub_string):
        return True
    return False


def set_upper(string: str):
    string = string.upper()
    return string


def find_index(full_command: list, string: str):
    char_to_find = command[1]
    index_found = string.index(char_to_find)
    return index_found


def cut_sting(full_command: list, string: str):
    start_index = int(command[1])
    next_count = int(command[2])
    part_to_preserve = string[start_index:]
    part_to_remove = part_to_preserve[next_count:]
    string = part_to_preserve.replace(part_to_remove, "")
    return string


text = input()

command = input().split()
while "Done" not in command:
    if "Change" == command[0]:
        text = change_string(command, text)
        print(text)

    elif "Includes" == command[0]:
        print(includes_check(command, text))

    elif "End" == command[0]:
        print(ends_check(command, text))

    elif "Uppercase" == command[0]:
        text = set_upper(text)
        print(text)

    elif "FindIndex" == command[0]:
        print(find_index(command, text))

    elif "Cut" == command[0]:
        text = cut_sting(command, text)
        print(text)

    command = input().split()
