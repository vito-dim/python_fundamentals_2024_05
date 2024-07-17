strings_list = []

command = input()
while command != 'end':
    current_string = command
    strings_list.append(current_string)

    command = input()

for string in strings_list:
    reversed_string = string[::-1]
    print(f'{string} = {reversed_string}')


# strings_list = []
#
# command = input()
# while command != 'end':
#     current_string = command
#     strings_list.append(current_string)
#
#     command = input()
#
# for string in strings_list:
#     reversed_string_list = [char for char in reversed(string)]
#     reversed_string = "".join(reversed_string_list)
#     print(f'{string} = {reversed_string}')


# strings_list = []
# strings_dict = dict()
#
# command = input()
# while command != 'end':
#     current_string = command
#     strings_list.append(current_string)
#
#     command = input()
#
# for string in strings_list:
#     reversed_string = string[::-1]
#     strings_dict[string] = reversed_string
#
# for (key, value) in strings_dict.items():
#     print(f'{key} = {value}')
