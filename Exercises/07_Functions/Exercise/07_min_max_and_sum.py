input_data = input().split()

data_as_int = list(int(digit) for digit in input_data)
min_num = min(data_as_int)
max_num = max(data_as_int)
sum_of_numbers = sum(data_as_int)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_of_numbers}")
