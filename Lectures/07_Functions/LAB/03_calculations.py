def calculate_operation(operation: str, num1: int, num2: int) -> int:
    """
    :param operation: (str) math operation, such as -> 'multiply', 'divide', 'add', and 'subtract'
    :param num1: (int) first number
    :param num2: (int) second number
    :return: (int) result from chosen math operation
    """
    result = None
    if operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = int(num1 / num2)
    elif operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2

    return result


operation_input = input()
first_number = int(input())
second_number = int(input())

print(calculate_operation(operation_input, first_number, second_number))

# Advance solution:
# def calculate_result(operator, num1, num2):
#     return {
#         'multiply': num1 * num2,
#         'divide': int(num1 / num2),
#         'add': num1 + num2,
#         'subtract': num1 - num2
#     }.get(operator, 'Invalid operator')
#
#
# input_operator = input('Enter the operator (multiply, divide, add or subtract): ')
# first_number = int(input('Enter first number: '))
# second_number = int(input('Enter second number: '))
# result = calculate_result(input_operator, first_number, second_number)
# print(result)
