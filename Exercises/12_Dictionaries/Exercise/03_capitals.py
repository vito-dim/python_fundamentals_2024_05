capitals = input().split(', ')
countries = input().split(', ')

countries_dict = {capitals[index]: countries[index] for index in range(len(capitals))}
for capital, country in countries_dict.items():
    print(f"{capital} -> {country}")

# capitals = input().split(', ')
# countries = input().split(', ')
#
# countries_dict = dict(zip(capitals, countries))
# for capital, country in countries_dict.items():
#     print(f"{capital} -> {country}")
