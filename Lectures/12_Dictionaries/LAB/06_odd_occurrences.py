words = input().split()
words_dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in words_dict:
        words_dict[word_lower] = 0
    words_dict[word_lower] += 1

for (key, value) in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

# odd_occurrences = []
# elements = input().split()
# elements_lower = [element.lower() for element in elements]
#
# for element in elements_lower:
#     if elements_lower.count(element) % 2 != 0:
#         if element not in odd_occurrences:
#             odd_occurrences.append(element)
#
# print(f'{" ".join(odd_occurrences)}')
