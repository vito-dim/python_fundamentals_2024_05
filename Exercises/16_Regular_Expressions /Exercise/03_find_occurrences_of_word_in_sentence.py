# import re
#
# sentence = input()
# word = input()
# pattern = rf'(?i)\b{word}\b'
# matches = re.findall(pattern, sentence)
# print(len(matches))

# import re
#
# sentence = input()
# word = input()
# pattern = rf"(?i)(\b{word}\b)"
# matches = [match.group() for match in re.finditer(pattern, sentence)]
# print(len(matches))

import re

sentence = input()
word = input()
pattern = rf"\b{word}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))
