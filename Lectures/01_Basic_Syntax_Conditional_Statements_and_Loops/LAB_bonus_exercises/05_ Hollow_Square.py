rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        pattern = '*'
        if i == 1 or i == rows:
            print(pattern, end='')
        else:
            if j == 1 or j == rows:
                print(pattern, end='')
            else:
                print(' ', end='')
    print()
