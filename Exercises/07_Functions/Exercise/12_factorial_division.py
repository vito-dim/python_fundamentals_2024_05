def factorial_calc(num_var: int) -> int:
    for current_num in range(1, num_var):
        num_var *= current_num
    return num_var


first_number = int(input())
second_number = int(input())
factorial_of_first = factorial_calc(first_number)
factorial_of_second = factorial_calc(second_number)
final_result = factorial_of_first / factorial_of_second
print(f'{final_result:.2f}')


# def calculate_factorial(some_number: int) -> int:
#     for current_number in range(1, some_number):
#         some_number *= current_number
#     return some_number
#
#
# first_number = int(input())
# second_number = int(input())
# first_factorial = calculate_factorial(first_number)
# second_factorial = calculate_factorial(second_number)
# print(f"{first_factorial / second_factorial:.2f}")
