# names = input().split(', ')
# sorted_names = sorted(names, key=lambda name: (-len(name), name))
# print(sorted_names)

def sort_names(list_var: list) -> list:
    # it will sort names, first by string length (from longest to shortest),
    # and then in case of duplicate length, will sort alphabetically
    sorted_names = sorted(list_var, key=lambda name: (-len(name), name))
    return sorted_names


names = input().split(', ')
result = sort_names(names)
print(result)
