def multiply_input_string(string_input: str, multiplier: int) -> str:
    """
    :param string_input: (str) input string provided from user
    :param multiplier: (int) counter, how many times to repeat the string
    :return: (str) modified_string = multiplied string
    """
    modified_string = string_input * multiplier
    return modified_string


input_string = input()
repeat_counter = int(input())
print(multiply_input_string(input_string, repeat_counter))

# Lambda function example:
# input_string = input()
# repeat_counter = int(input())
# multiply_string = lambda string, counter: string * counter
# result = multiply_string(input_string, repeat_counter)
# print(result)
