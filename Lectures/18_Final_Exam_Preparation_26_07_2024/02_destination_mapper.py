# import re
#
# pattern = r"(=|\/)?([A-Z][a-zA-Z]{2,})\1"
# string = input()
#
# valid_destinations = [destination[1] for destination in re.findall(pattern, string)]
# travel_points = sum(len(destination) for destination in valid_destinations)
#
# print(f"Destinations: {', '.join(valid_destinations)}")
# print(f"Travel Points: {travel_points}")

# import re
#
# pattern = r"([=\/])?([A-Z][a-zA-Z]{2,})\1"
# travel_points = 0
# string = input()
#
# valid_destinations = [destination.group(2) for destination in re.finditer(pattern, string)]
# for destination in valid_destinations:
#     travel_points += len(destination)
#
# print(f"Destinations: {', '.join(valid_destinations)}")
# print(f"Travel Points: {travel_points}")

import re

pattern = r"(=|\/)?([A-Z][a-zA-Z]{2,})\1"
travel_points = 0
string = input()

valid_destinations = [destination.group(2) for destination in re.finditer(pattern, string)]
for destination in valid_destinations:
    travel_points += len(destination)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
