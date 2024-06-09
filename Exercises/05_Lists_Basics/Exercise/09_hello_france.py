items_with_prices = input().split('|')
budget = float(input())

ticket_price = 150
max_clothes_price = 50.00
max_shoes_price = 35.00
max_accessories_price = 20.50

budget_left = budget
list_of_items_bought_with_modified_price = list()
total_items_sold_price = 0
profit = 0


for item_index in range(len(items_with_prices)):
    current_item_list = items_with_prices[item_index].split('->')
    current_item = current_item_list[0]
    current_item_price = float(current_item_list[1])
    max_item_price = 0

    if current_item.lower() == 'clothes':
        max_item_price = max_clothes_price
    elif current_item.lower() == 'shoes':
        max_item_price = max_shoes_price
    elif current_item.lower() == 'accessories':
        max_item_price = max_accessories_price

    if current_item_price <= max_item_price and current_item_price <= budget_left:
        budget_left -= current_item_price
        profit += 0.40 * current_item_price
        bought_item_with_new_price = (1 + 0.40) * current_item_price
        list_of_items_bought_with_modified_price.append(f'{bought_item_with_new_price:.2f}')


for item in list_of_items_bought_with_modified_price:
    total_items_sold_price += float(item)

for price_index in range(len(list_of_items_bought_with_modified_price)):
    if price_index != len(list_of_items_bought_with_modified_price) - 1:
        print(list_of_items_bought_with_modified_price[price_index], end=' ')
    else:
        print(list_of_items_bought_with_modified_price[price_index])

print(f"Profit: {profit:.2f}")

if total_items_sold_price + budget_left >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
