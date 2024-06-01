# string_count = int(input())
#
# special_symbols = [",", ".", "_"]
#
# for _ in range(1, string_count + 1):
#     is_pure = True
#     current_string = input()
#
#     for symbol in special_symbols:
#         if symbol in current_string:
#             is_pure = False
#
#     if is_pure:
#         print(f'{current_string} is pure.')
#     else:
#         print(f'{current_string} is not pure!')

strings_count = int(input())

for _ in range(1, strings_count + 1):
    current_string = input()

    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f'{current_string} is not pure!')

    else:
        print(f'{current_string} is pure.')
