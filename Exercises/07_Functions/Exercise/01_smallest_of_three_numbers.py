def smallest_of_three(num1: int, num2: int, num3: int) -> int:
    """
    Function that returns smallest number of three input int numbers
    :param num1: (int) first_number
    :param num2: (int) second_number
    :param num3: (int) third_number
    :return:
    """
    list_of_input_numbers = [num1, num2, num3]
    return min(list_of_input_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_of_three(first_number, second_number, third_number)

print(result)
