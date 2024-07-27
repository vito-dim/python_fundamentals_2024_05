# import re
#
# pattern = r"\d{2}(\/|\.|\-)[A-Z][a-z{2}]+\1\d{4}\b"
# text = input()
# for match in re.finditer(pattern, text):
#     current_match = match.group()
#     split_by = ''
#     if '/' in current_match:
#         split_by = '/'
#     elif '-' in current_match:
#         split_by = '-'
#     else:
#         split_by = '.'
#
#     current_match_list = current_match.split(split_by)
#     day, month, year = current_match_list
#     print(f"Day: {day}, Month: {month}, Year: {year}")

# import re
#
# regex_pattern = re.compile(pattern=r"(^|\b)(?P<day>\d{2})(\/|\.|\-)(?P<month>[A-Z][a-z{2}]+)\3(?P<year>\d{4})\b")
# text = input()
# matches = regex_pattern.finditer(text)
# for match in matches:
#     date = match.groupdict()
#     print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")

import re

regex_pattern = re.compile(pattern=r"(^|\b)(?P<day>\d{2})(\/|\.|\-)(?P<month>[A-Z][a-z{2}]+)\3(?P<year>\d{4})\b")
text = input()
matches = regex_pattern.finditer(text)
for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f"Day: {day}, Month: {month}, Year: {year}")
