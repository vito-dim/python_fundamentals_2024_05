def odd_and_even_sum(number: int) -> str:
    num_to_string = str(number)
    sum_of_even_digits = 0
    sum_of_odd_digits = 0

    for digit in num_to_string:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)

    odd_and_even_result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    return odd_and_even_result


input_number = int(input())

print(odd_and_even_sum(input_number))
