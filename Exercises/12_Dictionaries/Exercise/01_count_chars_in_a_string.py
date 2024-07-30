input_string = input().replace(' ', '')
char_dict = {}

for char in input_string:
    if char not in char_dict:
        char_dict[char] = input_string.count(char)

for char, count in char_dict.items():
    print(f"{char} -> {count}")
