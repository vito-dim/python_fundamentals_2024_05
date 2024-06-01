rows = int(input())
min_row = 1
max_row = rows

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == min_row or i == max_row:
            print('*', end='')
        else:
            if j == min_row or j == max_row:
                print('*', end='')
            else:
                print(' ', end='')
    print()
