number_of_electrons = int(input())
electrons_left = number_of_electrons
result = []
while electrons_left > 0:
    for i in range(1, electrons_left + 1):
        current_shell = 2 * (i ** 2)
        if electrons_left >= current_shell:
            result.append(current_shell)
            electrons_left -= current_shell
        else:
            if electrons_left == 0:
                break
            else:
                result.append(electrons_left)
                electrons_left -= electrons_left
                break

        if sum(result) == number_of_electrons:
            break

print(result)
