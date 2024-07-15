input_data = input().split()
bakery = {}

for index in range(0, len(input_data), 2):
    current_key = input_data[index]
    current_value = int(input_data[index + 1])
    bakery[current_key] = current_value

print(bakery)

# data = input().split()
# ingredients = [data[index] for index in range(len(data)) if index % 2 == 0]
# quantities = [int(data[index]) for index in range(len(data)) if index % 2 != 0]
# bakery = {}
#
# for index in range(len(ingredients)):
#     bakery[ingredients[index]] = quantities[index]
#
# print(bakery)

# data = input().split()
# ingredients = [data[index] for index in range(len(data)) if index % 2 == 0]
# quantities = [int(data[index]) for index in range(len(data)) if index % 2 != 0]
#
# bakery = dict(zip(ingredients, quantities))
#
# print(bakery)

# data = input().split()
# ingredients = [data[index] for index in range(len(data)) if index % 2 == 0]
# quantities = [int(data[index]) for index in range(len(data)) if index % 2 != 0]
#
# bakery = dict((ingredients[index], quantities[index]) for index in range(len(ingredients)))
#
# print(bakery)

# data = input().split()
# ingredients = [data[index] for index in range(len(data)) if index % 2 == 0]
# quantities = [int(data[index]) for index in range(len(data)) if index % 2 != 0]
#
# bakery = {key: value for key, value in zip(ingredients, quantities)}
#
# print(bakery)

# data = input().split()
# bakery = {}
# for index in range(0, len(data), 2):
#     bakery.update({data[index]: int(data[index + 1])})
#
# print(bakery)

# data = input().split()
# paired_data = list()
# bakery = dict()
#
# for index in range(0, len(data), 2):
#     current_pair = (data[index], int(data[index + 1]))
#     paired_data.append(current_pair)
#
# for key, value in paired_data:
#     bakery.update({key: value})
#
# print(bakery)
