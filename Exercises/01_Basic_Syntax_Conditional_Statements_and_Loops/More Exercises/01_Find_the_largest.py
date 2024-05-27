number = input()
number_digits_count = len(str(number))
digits_list = []
max_number = ''

for digit in range(number_digits_count):
    digits_list.append(number[digit])
