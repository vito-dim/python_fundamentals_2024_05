def perfect_number_fun(num: int) -> str:
    """
    Function that checks if number is perfect: it is a sum of its successful divisors
    :param num: (int) input number
    :return: (str) statement if number is perfect or not
    """
    num_list = [current_number for current_number in range(1, num)]
    successful_divisors = []

    for current_number in num_list:
        if number % current_number == 0:
            successful_divisors.append(current_number)

    if sum(successful_divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number_fun(number))

# def is_perfect(some_number: int) -> str:
#     divisors_sum = 0
#     for divisor in range(1, some_number):
#         if some_number % divisor == 0:
#             divisors_sum += divisor
#     if some_number == divisors_sum:
#         return "We have a perfect number!"
#     return "It's not so perfect."
#
#
# number = int(input())
# print(is_perfect(number))
