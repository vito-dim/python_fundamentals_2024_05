# notebook = {}
#
# words_and_definitions = input().split(" | ")
# for item in words_and_definitions:
#     word, word_definition = item.split(": ")
#     if word not in notebook:
#         notebook[word] = []
#     notebook[word].append(word_definition)
#
# test_words = input().split(" | ")
# command = input()  # "Test" or "Hand Over"
#
# if command == "Test":
#     for test_word in test_words:
#         if test_word in notebook:
#             print(f"{test_word}:")
#             for definition in notebook[test_word]:
#                 print(f" -{definition}")
#
# elif command == "Hand Over":
#     for word in notebook:
#         print(word, end=" ")
#
notebook = {}

words_and_definitions = input().split(" | ")
for item in words_and_definitions:
    word, word_definition = item.split(": ")
    if word not in notebook:
        notebook[word] = []
    notebook[word].append(word_definition)

test_words = input().split(" | ")
command = input()  # "Test" or "Hand Over"

for word, word_definition in notebook.items():
    if command == "Test" and word in test_words:
        print(f"{word}:")
        for definition in word_definition:
            print(f" -{definition}")

    elif command == "Hand Over":
        print(word, end=" ")
