# list_of_numbers = [int(number) for number in input().split(', ')]
# or
# list_of_numbers = list(map(int, input().split(', ')))
# indices_of_evens = []
# for index in range(len(list_of_numbers)):
#     if list_of_numbers[index] % 2 == 0:
#         indices_of_evens.append(index)
# print(indices_of_evens)


def index_of_even(list_var: list) -> list:
    result = [index for index in range(len(list_var)) if list_var[index] % 2 == 0]
    return result


list_of_numbers = list(map(int, input().split(', ')))
list_of_evens = index_of_even(list_of_numbers)
print(list_of_evens)
