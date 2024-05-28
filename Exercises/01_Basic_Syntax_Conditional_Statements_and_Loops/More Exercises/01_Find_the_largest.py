number_string = str(input())
sorted_string = sorted(number_string, reverse=True)
max_number = ''

for digit in sorted_string:
    max_number += digit

print(max_number)
