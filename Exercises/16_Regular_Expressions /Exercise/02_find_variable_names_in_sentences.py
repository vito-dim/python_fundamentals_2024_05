# import re
#
# text = input()
# pattern = r"\b_([a-zA-Z0-9]+)\b"
# matches = re.findall(pattern, text)
# print(",".join(matches))

# import re
#
# text = input()
# pattern = r"\b_{1}([a-zA-Z0-9]+)\b"
# matches = re.findall(pattern, text)
# print(*matches, sep=",")

# import re
#
# text = input()
# pattern = r"\b[_{1}]([a-zA-Z0-9]+)\b"
# matches = re.findall(pattern, text)
# print(*matches, sep=",")

# import re
#
# text = input()
# pattern = r"\b_([a-zA-Z0-9]+)\b"
# matches = re.finditer(pattern, text)
# # matches_found = [match.group() for match in matches]
# # print(*matches_found, sep=',')
# for current_match in matches:    # adds _
#     print(current_match.group())

# import re
#
# text = input()
# pattern = r"\b_(?P<valid>[a-zA-Z0-9]+)\b"
# matches = re.finditer(pattern, text)
# valid_matches = [element.group("valid") for element in matches]
# print(*valid_matches, sep=",")

# import re
#
# text = input()
# pattern = r"(?<= _{1})([a-zA-Z0-9]+)\b"
# matches = re.finditer(pattern, text)
# valid_matches = [match.group() for match in matches]
# print(*valid_matches, sep=",")

import re

text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_matches = [match.group() for match in re.finditer(pattern, text)]
# print(*valid_matches, sep=',')
print(','.join(valid_matches))
