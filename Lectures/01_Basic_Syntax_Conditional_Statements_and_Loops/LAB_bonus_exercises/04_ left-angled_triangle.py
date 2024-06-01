rows = int(input())

for i in range(rows + 1, 1, -1):
    for j in range(i, 1, -1):
        print('*', end='')
    print()
