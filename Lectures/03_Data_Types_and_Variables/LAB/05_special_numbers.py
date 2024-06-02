number = int(input())

for current_number in range(1, number + 1):
    current_number_as_string = str(current_number)
    current_digit_sum = 0

    for digit in current_number_as_string:
        current_digit_sum += int(digit)

    if current_digit_sum == 5 or \
            current_digit_sum == 7 or \
            current_digit_sum == 11:
        is_special = True
    else:
        is_special = False

    print(f'{current_number} -> {is_special}')
