# def only_evens(num_list: list) -> list:
#     list_of_evens = list()
#     for digit in num_list:
#         if int(digit) % 2 == 0:
#             list_of_evens.append(int(digit))
#
#     return list_of_evens
#
#
# number_sequence = input().split()
# print(only_evens(number_sequence))

def only_evens(number: int) -> bool:
    return number % 2 == 0


number_sequence = input().split()
number_int_list = list(map(int, number_sequence))
result = list(filter(only_evens, number_int_list))

print(result)


# is_even = lambda number: number % 2 == 0
# number_sequence = input().split()
# number_int_list = list(map(int, number_sequence))
# result = list(filter(is_even, number_int_list))
#
# print(result)
