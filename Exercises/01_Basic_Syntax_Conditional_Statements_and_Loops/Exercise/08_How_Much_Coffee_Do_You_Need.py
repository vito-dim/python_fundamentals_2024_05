# command = input()
#
# coffee_counter = 0
#
# while command != 'END':
#
#     if command.lower() == 'coding' or \
#             command.lower() in ['dog', 'cat'] or \
#             command.lower() == 'movie':
#         if command.islower():
#             coffee_counter += 1
#         else:
#             coffee_counter += 2
#
#     command = input()
#
# if coffee_counter > 5:
#     print('You need extra sleep')
# else:
#     print(coffee_counter)
#
#
command = input()

coffee_counter = 0

while command != 'END':

    if command.lower() in ['coding', 'dog', 'cat', 'movie']:
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
