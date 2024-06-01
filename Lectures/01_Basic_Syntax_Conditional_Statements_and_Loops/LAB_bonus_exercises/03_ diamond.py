rows = int(input())

for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(' ', end='')
    for k in range(0, i + 1):
        print('* ', end='')
    print()

for ri in range(0, rows - 1):
    for rj in range(0, ri + 1):
        print(' ', end='')
    for rk in range(0, rows - ri - 1):
        print('* ', end='')
    print()
