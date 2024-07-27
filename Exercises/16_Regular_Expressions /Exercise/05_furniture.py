# import re
#
# furniture_bought = []
# total_cost = 0
#
# pattern = r"\>{2}([a-zA-z]+)<{2}(\d+[\.]?\d+)\!(\d+$)"
#
# command = input()
# while command != "Purchase":
#     match = re.search(pattern, command)
#     if match:
#         furniture, price, quantity = match.groups()
#         total_cost += float(price) * int(quantity)
#         furniture_bought.append(furniture)
#     command = input()
#
# print("Bought furniture:")
# for item in furniture_bought:
#     print(item)
# print(f"Total money spend: {total_cost:.2f}")

# import re
#
# furniture_bought = []
# total_cost = 0
#
# pattern = r"(^|\b)\>{2}(?P<name>[a-zA-z]+)<{2}(?P<price>\d+[\.]?\d+)\!(?P<quantity>\d+$)"
# regex_pattern = re.compile(pattern)
#
# command = input()
# while command != "Purchase":
#     match = regex_pattern.finditer(command)
#     if match:
#         for element in match:
#             data = element.groupdict()
#             furniture_bought.append(data["name"])
#             total_cost += float(data["price"]) * int(data["quantity"])
#     command = input()
#
# print("Bought furniture:")
# for item in furniture_bought:
#     print(item)
# print(f"Total money spend: {total_cost:.2f}")

# import re
#
# furniture_bought = []
# money_spent = 0
# regex_pattern = re.compile(pattern=r"(^|\b)\>{2}([a-zA-z]+)<{2}(\d+[\.]?\d+)\!(\d+$)")
#
# furniture_information = input()
# while not furniture_information == "Purchase":
#     match = regex_pattern.finditer(furniture_information)
#     if match:
#         for element in match:
#             furniture_bought.append(element.group(2))
#             money_spent += float(element.group(3)) * int(element.group(4))
#
#     furniture_information = input()
#
# print("Bought furniture:")
# for item in furniture_bought:
#     print(item)
# print(f"Total money spend: {money_spent:.2f}")

import re

furniture_bought = []
money_spent = 0
regex_pattern = re.compile(pattern=r"(^|\b)\>{2}([a-zA-z]+)<{2}(\d+[\.]?\d+)\!(\d+$)")

furniture_information = input()
while not furniture_information == "Purchase":
    match = regex_pattern.match(furniture_information)
    if match:
        data = [element for element in match.groups() if element != ""]
        furniture_type, price, quantity = data
        furniture_bought.append(furniture_type)
        money_spent += float(price) * int(quantity)

    furniture_information = input()

print("Bought furniture:")
for item in furniture_bought:
    print(item)
print(f"Total money spend: {money_spent:.2f}")
