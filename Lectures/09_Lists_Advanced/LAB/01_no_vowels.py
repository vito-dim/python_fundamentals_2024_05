# basic example
input_text = input()

list_of_vowels = ['a', 'o', 'u', 'e', 'i']
list_without_vowels = [char for char in input_text if char.lower() not in list_of_vowels]
output_string = ''.join(list_without_vowels)
print(output_string)

# function
# def vowel_filter_func(char_var: str) -> str:
#     list_of_vowels = ['a', 'o', 'u', 'e', 'i']
#     if char_var.lower() not in list_of_vowels:
#         return char_var
#     else:
#         return ''
#
#
# input_text = input()
#
# list_without_vowels = [vowel_filter_func(char) for char in input_text]
# output_string = ''.join(list_without_vowels)
# print(output_string)
