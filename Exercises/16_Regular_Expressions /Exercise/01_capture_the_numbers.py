# import re
#
# line = input()
# while line:
#     pattern = r'\d+'
#     matches = re.findall(pattern, line)
#     if matches:
#         print(" ".join(matches), end=' ')
#     line = input()

# import re
#
# pattern = r"\d+"
# numbers_found = []
# line = input()
# while line:
#     matches = re.findall(pattern, line)
#     numbers_found.extend(matches)
#     line = input()
#
# print(*numbers_found, end=" ")

# import re
#
# pattern = r"(\d+)"
# numbers_found = []
#
# line = input()
# while line:
#     matches = re.finditer(pattern, line)
#     data = [element.group() for element in matches]
#     if data:
#         numbers_found.extend(data)
#
#     line = input()
#
# print(*numbers_found, end=" ")

# import re
#
# pattern = r"(\d+)"
#
# line = input()
# while line:
#     matches = re.finditer(pattern, line)
#     data = [element.group() for element in matches]
#     if data:
#         print(*data, end=" ")
#
#     line = input()

import re

regex_pattern = re.compile(pattern=r"\d+")

line = input()
while line:
    matches = regex_pattern.findall(line)
    if matches:
        print(*matches, end=" ")

    line = input()
