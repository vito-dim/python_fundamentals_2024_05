def char_in_range(char1: str, char2: str) -> str:
    start = ord(char1)
    stop = ord(char2)
    list_of_digits = []

    for digit in range(start + 1, stop):
        list_of_digits.append(digit)

    list_of_symbols = [chr(digit) for digit in list_of_digits]
    list_to_string = ' '.join(list_of_symbols)
    return list_to_string


first_char = input()
second_char = input()

result = char_in_range(first_char, second_char)
print(result)
