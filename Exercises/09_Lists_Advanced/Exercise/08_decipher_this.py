secret_message_list = input().split()
decrypted_message = []

for index in range(len(secret_message_list)):
    current_word = secret_message_list[index]
    current_word_length = len(current_word)
    first_letter_as_list = []
    second_part_as_list = []

    for letter in current_word:
        if letter.isdigit():
            first_letter_as_list.append(letter)
        else:
            second_part_as_list.append(letter)

    size_of_first_letter = len(first_letter_as_list) - 1
    first_letter_as_string = ''.join(first_letter_as_list)
    second_part_as_list[0], second_part_as_list[-1] = second_part_as_list[-1], second_part_as_list[0]
    first_letter = chr(int(first_letter_as_string))
    second_part_as_string = ''.join(second_part_as_list)
    decrypted_word = first_letter + second_part_as_string
    decrypted_message.append(decrypted_word)

decrypted_message_as_string = ' '.join(decrypted_message)
print(decrypted_message_as_string)
