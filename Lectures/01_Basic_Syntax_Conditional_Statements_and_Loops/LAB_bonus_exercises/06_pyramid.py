rows = int(input())

for i in range(1, rows + 1):
    # leading spaces
    for j in range(rows - i):
        print(' ', end='')
    # pattern for the current row
    for k in range(1, 2 * i):
        print('*', end='')
    print()
