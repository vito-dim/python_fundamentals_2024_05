# list_of_strings = input().split()
# special_palindrome = input()
# list_of_palindromes = []
# special_counter = 0
#
# for current_string in list_of_strings:
#     if current_string == current_string[::-1]:
#         list_of_palindromes.append(current_string)
#     if current_string == special_palindrome:
#         special_counter += 1
#
# print(list_of_palindromes)
# print(f"Found palindrome {special_counter} times")

words = input().split()
palindrome = input()

list_of_palindromes = list(current_word for current_word in words if current_word == current_word[::-1])
palindrome_count = list_of_palindromes.count(palindrome)

print(list_of_palindromes)
print(f'Found palindrome {palindrome_count} times')
