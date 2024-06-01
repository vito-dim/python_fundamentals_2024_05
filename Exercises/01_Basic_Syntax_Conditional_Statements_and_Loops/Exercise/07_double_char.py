# command = input()
#
# while command != 'End':
#     current_string = command
#
#     if current_string == 'SoftUni':
#         command = input()
#         continue
#
#     else:
#         modified_string = ''
#         for letter in range(len(current_string)):
#             modified_string += current_string[letter] * 2
#
#     print(modified_string)
#
#     command = input()

current_string = input()

while current_string != 'End':
    if current_string != 'SoftUni':
        modified_string = ''
        for letter in current_string:
            modified_string += letter * 2

        print(modified_string)

    current_string = input()
