def absolute_values(input_list: list) -> list:
    list_of_floats = list()
    list_of_absolute_values = list()

    for digit in input_list:
        list_of_floats.append(float(digit))

    for digit in list_of_floats:
        list_of_absolute_values.append(abs(digit))

    return list_of_absolute_values


input_data = input().split()

print(absolute_values(input_data))


# input_data = input().split()
# list_of_floats = list()
# list_of_absolute_values = list()
#
# for digit in input_data:
#     list_of_floats.append(float(digit))
#
# for digit in list_of_floats:
#     list_of_absolute_values.append(abs(digit))
#
# print(list_of_absolute_values)
