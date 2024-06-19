# numbers_list = [int(number) for number in input().split(' ')]
# average_of_nums = sum(numbers_list) / len(numbers_list)
# numbers_greater_than_average = [number for number in numbers_list if number > int(average_of_nums)]
# numbers_greater_than_average.sort(reverse=True)
# top_five = numbers_greater_than_average[:5]
#
# if len(top_five) == 0:
#     print('No')
# else:
#     print(*top_five, sep=' ')

numbers_list = [int(number) for number in input().split(' ')]
average_of_nums = sum(numbers_list) / len(numbers_list) if numbers_list else 0
numbers_greater_than_average = [number for number in numbers_list if number > int(average_of_nums)]

if numbers_greater_than_average:
    top_five = sorted(numbers_greater_than_average, reverse=True)[:5]
    print(*top_five, sep=' ')
else:
    print('No')
