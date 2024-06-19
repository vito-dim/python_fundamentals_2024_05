# text = input()
# filtered_words = list(word for word in text.split() if len(word) % 2 == 0)
# print('\n'.join(filtered_words))

# text = input()
# filtered_words = list(word for word in text.split() if len(word) % 2 == 0)
# for word in filtered_words:
#     print(word)

def filter_words(string_var: str) -> str:
    """
    Function that prints only words with even length on a new line each
    :param string_var: (str) input text
    :return: (str) modified string, containing the filtered words
    """
    filtered_words = [word for word in string_var.split() if len(word) % 2 == 0]
    return '\n'.join(filtered_words)


text = input()
filtered_result = filter_words(text)
print(filtered_result)
