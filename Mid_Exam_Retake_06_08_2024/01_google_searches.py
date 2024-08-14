money_per_search = float(input())
num_of_users = int(input())
total_money = 0

for index in range(num_of_users):
    no_fees = False
    current_user = index + 1
    searches = int(input())
    current_money_per_search = money_per_search

    if current_user % 3 == 0:
        current_money_per_search *= 3

    if searches > 5:
        current_money_per_search *= 2
    elif searches <= 1:
        no_fees = True

    if no_fees:
        continue
    else:
        cost = current_money_per_search * searches
        total_money += cost

print(f"Total money earned: {total_money:.2f}")
