# number = int(input())
# # 97 - 122
# for first in range(0, number):
#     for second in range(0, number):
#         for third in range(0, number):
#             print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')

# number = int(input())
# for first in range(0, number):
#     current_first = chr(97 + first)
#     for second in range(0, number):
#         current_second = chr(97 + second)
#         for third in range(0, number):
#             current_third = chr(97 + third)
#             print(f'{current_first}{current_second}{current_third}')

number = int(input())
for first in range(97, 97 + number):
    for second in range(97, 97 + number):
        for third in range(97, 97 + number):
            print(f'{chr(first)}{chr(second)}{chr(third)}')
