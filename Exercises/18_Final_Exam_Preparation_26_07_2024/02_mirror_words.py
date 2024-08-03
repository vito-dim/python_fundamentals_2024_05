# import re
#
# text = input()
# # pattern = r"#[a-zA-Z]{3,}##?[a-zA-Z]{3,}#|@[a-zA-Z]{3,}@@?[a-zA-Z]{3,}@"
# pattern = r"(?P<sep>@|#)(?P<word1>[a-zA-Z]{3,})\1\1(?P<word2>[a-zA-Z]{3,})\1"
# matches_obj = re.finditer(pattern, text)
# matches = []
# mirror_pairs = []
# for match in matches_obj:
#     matches.append(match.groupdict())
#
# for match in matches:
#     if match["word1"] == match["word2"][::-1] or match["word1"][::-1] == match["word2"]:
#         mirror_pair_found = f"{match['word1']} <=> {match['word2']}"
#         mirror_pairs.append(mirror_pair_found)
#
# if matches:
#     print(f"{len(matches)} word pairs found!")
# else:
#     print("No word pairs found!")
#
# if mirror_pairs:
#     print(f"The mirror words are:\n{', '.join(mirror_pairs)}")
# else:
#     print("No mirror words!")

import re

text = input()
pattern = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
matches = re.findall(pattern, text)
mirror_pairs = []

for match in matches:
    first_word = match[1]
    second_word = match[2]

    if first_word == second_word[::-1]:
        mirror_pair_found = f"{first_word} <=> {second_word}"
        mirror_pairs.append(mirror_pair_found)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_pairs:
    print(f"The mirror words are:\n{', '.join(mirror_pairs)}")
else:
    print("No mirror words!")

