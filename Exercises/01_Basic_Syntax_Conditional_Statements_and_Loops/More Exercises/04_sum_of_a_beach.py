input_string = input()

words_list = ["Sand", "Water", "Fish", "Sun"]
input_word_length = len(input_string)
words_appear_times = 0

for word in words_list:
    list_word_length = len(word)

    for char in range(input_word_length):
        current_word = input_string[char:char + list_word_length]
        current_word_length = len(current_word)

        if current_word_length < list_word_length:
            break

        if word.lower() == current_word.lower():
            words_appear_times += 1

print(words_appear_times)
