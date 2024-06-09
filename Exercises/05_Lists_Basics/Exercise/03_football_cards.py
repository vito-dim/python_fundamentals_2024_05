# 80 / 100
# card_sequence = input().split()
#
# game_is_terminated = False
# first_team_eliminated_players = 0
# second_team_eliminated_players = 0
#
# for current_card in card_sequence:
#     current_card_list = current_card.split('-')
#
#     if 'A' in current_card_list:
#         first_team_eliminated_players += 1
#     elif 'B' in current_card_list:
#         second_team_eliminated_players += 1
#
#     if first_team_eliminated_players > 4 or second_team_eliminated_players > 4:
#         game_is_terminated = True
#         break
#
# first_team_remaining_players = 11 - first_team_eliminated_players
# second_team_remaining_players = 11 - second_team_eliminated_players
#
# print(f'Team A - {first_team_remaining_players}; Team B - {second_team_remaining_players}')
#
# if game_is_terminated:
#     print('Game was terminated')

eliminated_players = input().split()
first_team_players = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
second_team_players = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_is_terminated = False

for player in eliminated_players:
    if player in first_team_players:
        first_team_players.remove(player)
    elif player in second_team_players:
        second_team_players.remove(player)

    if len(first_team_players) < 7 or len(second_team_players) < 7:
        game_is_terminated = True
        break

print(f'Team A - {len(first_team_players)}; Team B - {len(second_team_players)}')

if game_is_terminated:
    print('Game was terminated')

# 80 / 100
# eliminated_players = input().split()
# team_a = []
# team_b = []
# game_terminated = False
#
# for team_index in range(len(eliminated_players)):
#     current_team_attributes = eliminated_players[team_index].split('-')
#     current_team = current_team_attributes[0]
#     if current_team.__contains__('A'):
#         team_a.append(eliminated_players[team_index])
#
#     else:
#         team_b.append(eliminated_players[team_index])
#
#     if len(team_a) > 4 or len(team_b) > 4:
#         game_terminated = True
#         break
#
# print(f'Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}')
#
# if game_terminated:
#     print('Game was terminated')
