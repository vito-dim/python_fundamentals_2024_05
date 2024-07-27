#1
import re

names = input()
regex_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(regex_pattern, names)

for name in matches:
    print(name, end=' ')

#2
import re

numbers = input()
regex_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex_pattern, numbers)
print(', '.join(matches))

#3
import re

data = input()
regex_pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
matches = re.finditer(regex_pattern, data)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')
