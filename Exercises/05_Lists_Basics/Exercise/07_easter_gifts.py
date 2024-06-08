# gifts_list = input().split()
#
# command = input()
# while command != "No Money":
#     current_command = command.split()
#     gift_from_command = current_command[1]
#
#     if "OutOfStock" in current_command:
#         for gift_index, gift in enumerate(gifts_list):
#             if gift == gift_from_command:
#                 gifts_list[gift_index] = 'None'
#
#     elif "Required" in current_command:
#         gift_index_from_command = int(current_command[2])
#
#         if 0 <= gift_index_from_command <= len(gifts_list) - 1:
#             gifts_list[gift_index_from_command] = gift_from_command
#
#     elif "JustInCase" in current_command:
#         gifts_list[-1] = gift_from_command
#
#     command = input()
#
# duplicate_count = gifts_list.count("None")
# if duplicate_count > 0:
#     for remove in range(duplicate_count):
#         gifts_list.remove("None")
#
# gifts_to_string = " ".join(gifts_list)
# print(gifts_to_string)


gifts_list = input().split()

command = input()
while command != "No Money":
    current_command = command.split()
    gift_from_command = current_command[1]

    if "OutOfStock" in current_command:
        duplicate_count = gifts_list.count(gift_from_command)

        if duplicate_count > 0:
            for replace in range(duplicate_count):
                index_to_replace = gifts_list.index(gift_from_command)
                gifts_list[index_to_replace] = 'None'

    elif "Required" in current_command:
        gift_index_from_command = int(current_command[2])

        if 0 <= gift_index_from_command <= len(gifts_list) - 1:
            gifts_list[gift_index_from_command] = gift_from_command

    elif "JustInCase" in current_command:
        gifts_list[-1] = gift_from_command

    command = input()

duplicate_count = gifts_list.count("None")
if duplicate_count > 0:
    for remove in range(duplicate_count):
        gifts_list.remove("None")

gifts_to_string = " ".join(gifts_list)
print(gifts_to_string)
