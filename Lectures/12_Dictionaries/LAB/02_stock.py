data = input().split()
search_data = input().split()

stock_data_dict = {data[index]: data[index + 1] for index in range(0, len(data), 2)}

for product in search_data:
    if product in stock_data_dict:
        quantity = stock_data_dict[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# data = input().split()
# search_data = input().split()
#
# stock_data_dict = dict((data[index], data[index + 1]) for index in range(0, len(data), 2))
#
# for product in search_data:
#     if product in stock_data_dict:
#         quantity = stock_data_dict[product]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")


# stock_data = input().split()
# search_data = input().split()
#
# stock_data_dict = {}
# for index in range(0, len(stock_data), 2):
#     current_item, current_value = stock_data[index], int(stock_data[index + 1])
#     stock_data_dict[current_item] = current_value
#
# for product in search_data:
#     if product in stock_data_dict:
#         quantity = stock_data_dict[product]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
