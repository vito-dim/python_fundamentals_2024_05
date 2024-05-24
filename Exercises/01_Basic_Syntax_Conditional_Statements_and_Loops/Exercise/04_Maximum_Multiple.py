# divisor = int(input())
# boundary = int(input())
# max_number = 0
#
# for current_number in range(boundary, 0, -1):
#     if 0 < current_number <= boundary:
#         if current_number % divisor == 0:
#             max_number = current_number
#             break
#
# print(max_number)

divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor-1, -1):
    if number % divisor == 0:
        print(number)
        break
