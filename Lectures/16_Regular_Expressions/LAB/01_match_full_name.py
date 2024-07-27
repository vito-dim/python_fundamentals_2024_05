# import re
#
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = input()
# matches = re.findall(pattern, text)
# print(" ".join(matches))

# import re
#
# pattern = r"\b(?P<name>[A-Z][a-z]+) (?P<surname>[A-Z][a-z]+)\b"
# text = input()
# match_info = re.finditer(pattern, text)
# for match in match_info:
#     data = match.groupdict()
#     print(f"{data['name']} {data['surname']}", end=" ")

import re

pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
text = input()
matches_found = re.finditer(pattern, text)
for match in matches_found:
    print(match.group(1), end=' ')
