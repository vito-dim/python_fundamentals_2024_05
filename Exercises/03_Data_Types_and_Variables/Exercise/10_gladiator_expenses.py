# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# shield_counter = 0
# expenses = 0
#
# for fight in range(1, lost_fights_count + 1):
#     if fight % 2 == 0:
#         expenses += helmet_price
#     if fight % 3 == 0:
#         expenses += sword_price
#     if fight % 6 == 0:
#         expenses += shield_price
#         shield_counter += 1
#         if shield_counter % 2 == 0:
#             expenses += armor_price
# print(f'Gladiator expenses: {expenses:.2f} aureus')

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_counter = 0

total_helmet_broken = lost_fights_count // 2
total_sword_broken = lost_fights_count // 3
total_shield_broken = lost_fights_count // (2 * 3)
total_armor_broken = total_shield_broken // 2

expenses = total_helmet_broken * helmet_price \
           + total_sword_broken * sword_price \
           + total_shield_broken * shield_price \
           + total_armor_broken * armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
