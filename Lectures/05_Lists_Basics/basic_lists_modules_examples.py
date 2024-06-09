#             0             1           2          3            4          5
my_list = ["Eggs", "StuffedAnimal", "Cozonac", "Sweets", "EasterBunny", "Eggs"]
print(my_list)
# List index of Eggs - first occurrence
print(my_list.index("Eggs"))
# List count
print(my_list.count("Eggs"))
# List len
print(len(my_list))
# List type(len)
print(type(len(my_list)))
# Reverse list by slicing
print(my_list[::-1])
# Reverse list by using reversed function
print(list(reversed(my_list)))
# Reverse list by using reverse method. !!! Method is used directly on list itself to take effect
my_list.reverse()
print(my_list)
#             0             1           2          3            4          5
my_list2 = ["Eggs", "StuffedAnimal", "Cozonac", "Sweets", "EasterBunny", "Eggs"]
print(my_list2)
# append
my_list2.append("whiskey")
print(my_list2)
# clear
my_list2.clear()
print(my_list2)
# copy
my_list2 = my_list.copy()
print(my_list2)
# extend
dummy_list = ['top', 'course']
my_list2.extend(dummy_list)
print(my_list2)
# insert
my_list2.insert(1, 'test')
print(my_list2)
# pop
my_list2.pop(1)
print(my_list2)
# remove - will remove first occurrence of the value
my_list2.remove('Eggs')
# sort
my_list2.sort()
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)
