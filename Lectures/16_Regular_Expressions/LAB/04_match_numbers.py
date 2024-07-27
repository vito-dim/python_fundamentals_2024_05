# import re
#
# pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
# text = input()
# matches = [match.group() for match in re.finditer(pattern, text)]
# # print(' '.join(matches))
# print(*matches, sep=' ')

import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), end=' ')
