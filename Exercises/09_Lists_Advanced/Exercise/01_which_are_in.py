# substring_list = input().split(', ')
# main_string_list = input().split(', ')
# subs_that_are_in = []
#
# for sub in substring_list:
#     for main in main_string_list:
#         if sub in main:
#             subs_that_are_in.append(sub)
#             break
#
# print(subs_that_are_in)

# def which_are_in(sub_str_list: list, main_str_list: list) -> list:
#     subs_which_are_in = []
#     for sub in sub_str_list:
#         for main in main_str_list:
#             if sub in main:
#                 subs_which_are_in.append(sub)
#                 break
#
#     return subs_which_are_in
#
#
# substring_list = input().split(', ')
# main_string_list = input().split(', ')
# subs_that_are_in = which_are_in(substring_list, main_string_list)
# print(subs_that_are_in)


def which_are_in(sub_str_list: list, main_str_list: list) -> list:
    return [current_sub for current_sub in sub_str_list
            if any(current_sub in current_main for current_main in main_str_list)]


substring_list = input().split(', ')
main_string_list = input().split(', ')
subs_that_are_in = which_are_in(substring_list, main_string_list)
print(subs_that_are_in)
