# def loading_bar(num_var: int) -> str:
#     loading_status = None
#     loaded_percentage = None
#     result = None
#
#     if num_var == 100:
#         loading_status = f'{num_var}% Complete!'
#         loaded_percentage = '[%%%%%%%%%%]'
#         result = f'{loading_status}\n{loaded_percentage}'
#     else:
#         current_status = num_var // 10
#         progress_left = 10 - current_status
#         result = f'{num_var}% [{current_status * "%"}{progress_left * "."}]\nStill loading...'
#
#     return result
#
#
# number = int(input())
# print(loading_bar(number))

def loading_bar(num_var: int) -> str:
    result = None

    if num_var == 100:
        result = f'{num_var}% Complete!\n[%%%%%%%%%%]'
    else:
        current_status = num_var // 10
        progress_left = 10 - current_status
        result = f'{num_var}% [{current_status * "%"}{progress_left * "."}]\nStill loading...'

    return result


number = int(input())
print(loading_bar(number))

# def loading_bar(some_number) -> str:
#     if some_number == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#     loaded_percent_as_digit = some_number // 10
#     return f"{some_number}% [{'%' * loaded_percent_as_digit}{'.' * (10 - loaded_percent_as_digit)}]\nStill loading..."
#
#
# number = int(input())
# print(loading_bar(number))
