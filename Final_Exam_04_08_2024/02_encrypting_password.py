import re

input_counts = int(input())
regex_pattern = re.compile(
    pattern=r"(^.*)(>(?P<group1>\d{3})\|(?P<group2>[a-z]{3})\|(?P<group3>[A-Z]{3})\|(?P<group4>[^\<\>]{3})<)\1$")

for _ in range(input_counts):
    password = input()

    validity_matches = [match.groupdict() for match in regex_pattern.finditer(password)]
    if validity_matches:
        for valid_match in validity_matches:
            encrypted_password = (valid_match['group1']
                                  + valid_match['group2']
                                  + valid_match['group3']
                                  + valid_match['group4'])
            print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
