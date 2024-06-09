input_list_of_strings = input().split()
inverted_list_of_integers = []

for digit in input_list_of_strings:
    inverted_list_of_integers.append(-int(digit))

print(inverted_list_of_integers)
