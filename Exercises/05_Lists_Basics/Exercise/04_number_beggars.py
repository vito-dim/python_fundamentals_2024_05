money_earned_string = input().split(', ')
beggars_count = int(input())
money = list()
final_list = list()

for digit in money_earned_string:
    money.append(int(digit))

start_index = 0
for current_beggar in range(beggars_count):
    current_sum = 0
    for earned_by_current_beggar in range(start_index, len(money), beggars_count):
        current_sum += money[earned_by_current_beggar]
    final_list.append(current_sum)
    start_index += 1

print(final_list)
