def round_given_input(list_var: list) -> list:
    """
    Function that returns of rounded integers, by a given list
    :param list_var: (list) input list
    :return: (list) list of rounded values from input list
    """
    list_of_floats = list(map(float, list_var))
    list_of_rounded_integers = []

    for digit in list_of_floats:
        list_of_rounded_integers.append(round(digit))

    return list_of_rounded_integers


input_data = input().split()
result = round_given_input(list_var=input_data)
print(result)
