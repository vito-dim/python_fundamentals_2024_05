# def is_positive(number_list: list) -> str:
#     filtered_numbers = [number for number in number_list if number >= 0]
#     return ', '.join(map(str, filtered_numbers))
#
#
# def is_negative(number_list: list) -> str:
#     filtered_numbers = [number for number in number_list if number < 0]
#     return ', '.join(map(str, filtered_numbers))
#
#
# def is_even(number_list: list) -> str:
#     filtered_numbers = [number for number in number_list if number % 2 == 0]
#     return ', '.join(map(str, filtered_numbers))
#
#
# def is_odd(number_list: list) -> str:
#     filtered_numbers = [number for number in number_list if number % 2 != 0]
#     return ', '.join(map(str, filtered_numbers))
#
#
# list_of_numbers = list(map(int, input().split(', ')))
#
# print(f'Positive: {is_positive(list_of_numbers)}')
# print(f'Negative: {is_negative(list_of_numbers)}')
# print(f'Even: {is_even(list_of_numbers)}')
# print(f'Odd: {is_odd(list_of_numbers)}')


list_of_numbers = list(map(int, input().split(', ')))

POSITIVE = [str(number) for number in list_of_numbers if number >= 0]
NEGATIVE = [str(number) for number in list_of_numbers if number < 0]
EVEN = [str(number) for number in list_of_numbers if number % 2 == 0]
ODD = [str(number) for number in list_of_numbers if number % 2 != 0]

print(f"Positive: {', '.join(POSITIVE)}")
print(f"Negative: {', '.join(NEGATIVE)}")
print(f"Even: {', '.join(EVEN)}")
print(f"Odd: {', '.join(ODD)}")
