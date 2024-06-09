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
