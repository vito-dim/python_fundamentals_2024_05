# number_of_strings = int(input())
# special_word = input()
# list_of_strings = list()
# list_of_special_strings = list()
#
# for _ in range(number_of_strings):
#     current_string = input()
#     list_of_strings.append(current_string)
#
#     if special_word in current_string:
#         list_of_special_strings.append(current_string)
#
# print(f'{list_of_strings}\n{list_of_special_strings}')

number_of_strings = int(input())
special_word = input()
list_of_strings = list()

for _ in range(number_of_strings):
    current_string = input()
    list_of_strings.append(current_string)

print(list_of_strings)

for index in range(len(list_of_strings) - 1, -1, -1):
    list_element = list_of_strings[index]

    if special_word not in list_element:
        list_of_strings.remove(list_element)
print(list_of_strings)
