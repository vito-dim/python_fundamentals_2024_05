def sum_numbers(num1, num2):
    return num1 + num2


def subtract(returned_result, num3):
    return returned_result - num3


def add_and_subtract(num1, num2, num3):
    result_of_sum = sum_numbers(num1, num2)
    final_result = subtract(result_of_sum, num3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)

print(result)
