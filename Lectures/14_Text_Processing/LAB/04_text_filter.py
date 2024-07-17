banned_words = input().split(', ')
text = input()

for word in banned_words:
    censored_word = len(word) * '*'
    while word in text:
        text = text.replace(word, censored_word)

print(text)
