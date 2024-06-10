def is_palindrome(current_number: int) -> bool:
    """
    Function that checks if a number is palindrome
    :param current_number: (int) number
    :return: (bool) True or False, if number is palindrome or not
    """
    return str(current_number) == str(current_number)[::-1]


input_list_of_numbers = input().split(', ')
list_of_int_numbers = list(map(int, input_list_of_numbers))
for digit in list_of_int_numbers:
    print(is_palindrome(digit))


# def is_palindrome(some_number_as_string):
#     return some_number_as_string == some_number_as_string[::-1]
#
#
# numbers_as_string = input().split(", ")
# for number in numbers_as_string:
#     print(is_palindrome(number))
#