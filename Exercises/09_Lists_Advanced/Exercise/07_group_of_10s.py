list_of_numbers = list(int(number) for number in input().split(', '))
boundary = 10
group = []

while list_of_numbers:
    for index in range(len(list_of_numbers)):
        current_number = list_of_numbers[index]
        if list_of_numbers[index] <= boundary:
            group.append(current_number)

    print(f"Group of {boundary}'s: {group}")

    list_of_numbers = [number for number in list_of_numbers if number > boundary]
    group.clear()
    boundary += 10

# def group_numbers(int_list: list) -> list:
#     group_boundary = 10
#     result = []
#
#     while int_list:
#         group = [num for num in int_list if num <= group_boundary]
#         int_list = [num for num in int_list if num > group_boundary]
#         result.append(f"Group of {group_boundary}'s: {group}")
#         group_boundary += 10
#
#     return result
#
#
# input_num_data = list(map(int, input().split(', ')))
# grouped_numbers = group_numbers(input_num_data)
#
# for current_group in grouped_numbers:
#     print(current_group)
