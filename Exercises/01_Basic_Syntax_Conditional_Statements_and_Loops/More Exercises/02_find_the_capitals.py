input_string = input()
string_length = len(input_string)
list_capitals = []

for char_index in range(string_length):
    if input_string[char_index].isupper():
        list_capitals.append(char_index)

print(list_capitals)
