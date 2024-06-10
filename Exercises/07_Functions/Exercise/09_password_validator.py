def generate_valid_list(start_range: int, stop_range: int):
    generated_list = []
    for char in range(start_range, stop_range + 1):
        generated_list.append(chr(char))
    return generated_list


def pass_validator(pass_var: str) -> str:
    is_valid = True
    list_of_pass_symbols = [digit for digit in pass_var]
    list_of_possible_options = [str(digit) for digit in range(10)]
    digit_counter = 0
    validation_result = None
    final_result_as_string = None
    final_result = ["Password is valid"]
    list_of_capital_letters = generate_valid_list(65, 90)
    list_of_small_letters = generate_valid_list(97, 122)
    list_of_possible_options += (list_of_small_letters + list_of_capital_letters)

    if not 6 <= len(list_of_pass_symbols) <= 10:
        is_valid = False
        validation_result = 'Password must be between 6 and 10 characters'
        final_result.append(validation_result)

    for digit in list_of_pass_symbols:
        if digit not in list_of_possible_options:
            is_valid = False
            validation_result = 'Password must consist only of letters and digits'
            final_result.append(validation_result)

        if digit in list_of_possible_options:
            if digit.isdigit():
                digit_counter += 1
            if digit_counter < 2 and digit == list_of_pass_symbols[-1]:
                is_valid = False
                validation_result = 'Password must have at least 2 digits'
                final_result.append(validation_result)
                break

    if is_valid:
        final_result_as_string = '\n'.join(final_result)
    else:
        final_result.pop(0)
        final_result_as_string = '\n'.join(final_result)

    return final_result_as_string


password = input()
print(pass_validator(password))
