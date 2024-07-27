# import re
#
# text = input()
# pattern = r"(^| )(?P<user>[a-z0-9]+[\.|\_|\-]?[a-z0-9]+)@(?P<host>[a-z-]+(\.[a-z]+)+)"
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(f"{match.group('user')}@{match.group('host')}")
#
# import re
#
# text = input()
# pattern = r"\s(([a-z0-9]+[\.|\_|\-]?[a-z0-9]+)@([a-z-]+(\.[a-z]+)+))\b"
# matches = re.findall(pattern, text)
# for match in matches:
#     print(match[0])
#     # print(len(match))
#     # print(match)

# import re
#
# text = input()
# pattern = r"(^| )(?P<user>[a-z0-9]+[\.|\_|\-]?[a-z0-9]+)@(?P<host>[a-z-]+(\.[a-z]+)+)"
# matches = re.finditer(pattern, text)
# for match in matches:
#     data = match.groupdict()
#     print(f"{data['user']}@{data['host']}")

import re

text = input()
pattern = r"(^|(?<=\s)[a-z0-9]+[\.|\_|\-]?[a-z0-9]+)@[a-z]+-?[a-z]+(\.[a-z]+)+"
valid_mails = [mail.group() for mail in re.finditer(pattern, text)]
print(*valid_mails, sep="\n")
