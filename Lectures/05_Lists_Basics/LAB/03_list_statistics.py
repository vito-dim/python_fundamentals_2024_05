# numbers_count = int(input())
# positive_numbers = []
# count_positives = 0
# negative_numbers = []
# sum_of_negatives = 0
#
# for _ in range(numbers_count):
#     current_number = int(input())
#
#     if current_number >= 0:
#         positive_numbers.append(current_number)
#         count_positives += 1
#
#     else:
#         negative_numbers.append(current_number)
#         sum_of_negatives += current_number
#
# print(positive_numbers)
# print(negative_numbers)
# print(f'Count of positives: {count_positives}')
# print(f'Sum of negatives: {sum_of_negatives}')

numbers_count = int(input())
positive_numbers = []
negative_numbers = []

for _ in range(numbers_count):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)

    else:
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}')
