# 1

list_with_numbers = input().split()
opposite_numbers = []  # opposite_numbers = list
for number in list_with_numbers:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)

# 2

factor = int(input())
count = int(input())
numbers = []
for multiplier in range(1, count + 1):
    numbers.append(factor * multiplier)
print(numbers)

# 3
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_was_terminated = False
players = input().split()
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")

# 4

money_as_string = input().split(", ")
number_of_beggars = int(input())
# money_as_integer = [int(money) for money in money_as_string]
money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))
final_list = []
start_index = 0
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_list.append(current_beggar_sum)
    start_index += 1
print(final_list)

# 5

deck_of_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):  # len(right_part)
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling
print(deck_of_cards)

# 10


events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    value_of_event = int(event_items[1])
    if type_of_event == "rest":
        initial_energy = total_energy
        total_energy += value_of_event
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_coins += value_of_event
            total_energy -= 30
            print(f"You earned {value_of_event} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= value_of_event:
            total_coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:  # if bakery_is_open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

else:  # if bakery_is_open == False
    print(f"Closed! Cannot afford {type_of_event}.")