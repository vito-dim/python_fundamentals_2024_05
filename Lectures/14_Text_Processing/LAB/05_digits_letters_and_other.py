data = input()
digits = ''
letters = ''
other_chars = ''

for symbol in data:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_chars += symbol

print(digits)
print(letters)
print(other_chars)
