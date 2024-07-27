# import re
#
# pattern = r"\+359(\s|-)2\1([0-9]{3})\1([0-9]{4})\b"
# text = input()
# matches = [match.group() for match in re.finditer(pattern, text)]
# print(*matches, sep=', ')

# import re
#
# pattern = r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b"
# text = input()
# matches = re.findall(pattern, text)
# print(", ".join(matches))

# import re
#
# pattern = r"(\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4})\b"
# text = input()
# matches = re.findall(pattern, text)
# print(", ".join(matches))

import re

pattern = r"(\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4})\b"
text = input()
matches = [match.group(1) for match in re.finditer(pattern, text)]
print(", ".join(matches))
