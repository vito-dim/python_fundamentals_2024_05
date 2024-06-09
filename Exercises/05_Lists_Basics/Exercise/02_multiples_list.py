number_factor = int(input())
number_count = int(input())
multiples_list = list()

for number in range(1, number_count + 1):
    multiple_number = number * number_factor
    multiples_list.append(multiple_number)

print(multiples_list)
