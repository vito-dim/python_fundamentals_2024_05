# def sort_input_string(string: str) -> list:
#     """
#     Function that converts input string of numbers in list of integers and sorts it ascending
#     :param string: (str) input data
#     :return: list of ascending sorted integers
#     """
#     list_from_data_as_string = string.split()
#     list_from_data_as_int = list(map(int, list_from_data_as_string))
#     list_from_data_as_int.sort()
#     return list_from_data_as_int
#
#
# data = input()
# print(sort_input_string(data))


def sort_input_string(string: str) -> list:
    """
    Function that converts input string of numbers in list of integers and sorts it ascending
    :param string: (str) input data
    :return: list of ascending sorted integers
    """
    list_from_data_as_string = string.split()
    list_from_data_as_int = list(map(int, list_from_data_as_string))
    list_sorted_ascending = sorted(list_from_data_as_int)
    return list_sorted_ascending


data = input()
print(sort_input_string(data))

# data = input().split()
# data_as_int = [int(digit) for digit in data]
# print(sorted(data_as_int))
