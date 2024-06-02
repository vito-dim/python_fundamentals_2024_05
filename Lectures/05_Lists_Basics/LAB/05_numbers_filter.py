# numbers_count = int(input())
# numbers_list = []
#
# for _ in range(numbers_count):
#     current_number = int(input())
#     numbers_list.append(current_number)
#
# command = input()
#
# for index in range(len(numbers_list) - 1, -1, -1):
#     list_element = numbers_list[index]
#     if command == 'even':
#         if list_element % 2 != 0:
#             numbers_list.remove(list_element)
#     elif command == 'odd':
#         if list_element % 2 == 0:
#             numbers_list.remove(list_element)
#     elif command == 'negative':
#         if list_element >= 0:
#             numbers_list.remove(list_element)
#     elif command == 'positive':
#         if list_element < 0:
#             numbers_list.remove(list_element)
#
# print(numbers_list)

# numbers_count = int(input())
# numbers_list = []
#
# for _ in range(numbers_count):
#     current_number = int(input())
#     numbers_list.append(current_number)
#
# command = input()
#
# for index in range(len(numbers_list) - 1, -1, -1):
#     list_element = numbers_list[index]
#
#     if (command == 'even') and (list_element % 2 != 0):
#         numbers_list.remove(list_element)
#     elif (command == 'odd') and (list_element % 2 == 0):
#         numbers_list.remove(list_element)
#     elif (command == 'negative') and (list_element >= 0):
#         numbers_list.remove(list_element)
#     elif (command == 'positive') and (list_element < 0):
#         numbers_list.remove(list_element)
#
# print(numbers_list)

numbers_count = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

numbers_list = [int(input()) for _ in range(numbers_count)]

command = input()

filtered_numbers = list()

for number in numbers_list:
    filtered_command = (
            (command == COMMAND_EVEN and number % 2 == 0) or
            (command == COMMAND_ODD and number % 2 != 0) or
            (command == COMMAND_NEGATIVE and number < 0) or
            (command == COMMAND_POSITIVE and number >= 0)
    )

    if filtered_command:
        filtered_numbers.append(number)

print(filtered_numbers)
