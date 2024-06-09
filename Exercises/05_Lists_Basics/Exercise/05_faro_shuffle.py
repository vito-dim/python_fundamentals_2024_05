deck_of_cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    deck_middle = len(deck_of_cards) // 2
    left_part = deck_of_cards[:deck_middle]
    right_part = deck_of_cards[deck_middle:]
    shuffled_deck = []

    for card_index in range(len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append((right_part[card_index]))

    deck_of_cards = shuffled_deck

print(deck_of_cards)
