# pattern_number = int(input())
# pattern = ''
#
# for index in range(1, pattern_number + 1):
#     pattern = '*' * index
#     print(pattern)
#
# for index in range(pattern_number - 1, 0, -1):
#     pattern = '*' * index
#     print(pattern)

# version 2
number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
