# import re
#
# pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
# valid_mails = []
# text = input()
# while text:
#     matches = re.finditer(pattern, text)
#     if matches:
#         current_matches = [match.group() for match in matches]
#         valid_mails.extend(current_matches)
#
#     text = input()
#
# for mail in valid_mails:
#     print(mail)

# import re
#
# regex_pattern = re.compile(pattern=r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+")
# valid_mails = []
#
# text = input()
# while text:
#     matches_found = [match.group() for match in regex_pattern.finditer(text)]
#     if matches_found:
#         valid_mails.extend(matches_found)
#
#     text = input()
#
# print(*valid_mails, sep='\n')

# import re
#
# regex_pattern = re.compile(pattern=r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+")
#
# text = input()
# while text:
#     matches = regex_pattern.search(text)
#     if matches:
#         print(matches[0])
#     text = input()

import re

pattern = r"(w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+)"

text = input()
while text:
    valid_matches = re.search(pattern, text)
    if valid_matches:
        url = valid_matches.group(1)
        print(url)
    text = input()
