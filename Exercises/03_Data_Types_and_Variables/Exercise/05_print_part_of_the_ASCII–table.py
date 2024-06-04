# start_index = int(input())
# stop_index = int(input())
#
# for index in range(start_index, stop_index + 1):
#     current_char = chr(index)
#     print(f'{current_char}', end=' ')

start_index = int(input())
stop_index = int(input())
lst_of_characters = []

for index in range(start_index, stop_index + 1):
    lst_of_characters.append(chr(index))

print(' '.join(lst_of_characters))
