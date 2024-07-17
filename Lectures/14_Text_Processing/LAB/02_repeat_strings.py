strings_list = input().split()
repeated_string = ''
for string in strings_list:
    repeater = len(string)
    repeated_string += string * repeater

print(repeated_string)
