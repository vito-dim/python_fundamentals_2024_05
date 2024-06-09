# list_as_string = input().split()
# numbers_to_remove = int(input())
# list_as_int = list()
#
# for digit in list_as_string:
#     list_as_int.append(int(digit))
#
# for _ in range(numbers_to_remove):
#     current_min = min(list_as_int)
#     list_as_int.remove(current_min)
#
# for index in range(len(list_as_int)):
#     if index == len(list_as_int) - 1:
#         print(list_as_int[index])
#     else:
#         print(list_as_int[index], end=", ")

list_of_integers = [int(digits) for digits in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    current_min_number = min(list_of_integers)
    list_of_integers.remove(current_min_number)

for index in range(len(list_of_integers)):
    if index != len(list_of_integers) - 1:
        print(list_of_integers[index], end=", ")
    else:
        print(list_of_integers[index])
