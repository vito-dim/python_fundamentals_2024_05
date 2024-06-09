working_day_events = input().split('|')
initial_energy = 100
initial_coins = 100

energy = initial_energy
coins = initial_coins
bakery_is_closed = False

for current_day_index in range(len(working_day_events)):
    current_day_attributes = working_day_events[current_day_index].split('-')
    current_day_event = current_day_attributes[0]
    current_day_value = int(current_day_attributes[1])

    if current_day_event == 'rest':
        initial_energy = energy
        energy += current_day_value
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif current_day_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += current_day_value
            earned = current_day_value
            print(f'You earned {earned} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        ingredient = current_day_event
        ingredient_price = current_day_value

        if coins >= ingredient_price:
            coins -= ingredient_price
            print(f'You bought {ingredient}.')
        else:
            print(f'Closed! Cannot afford {ingredient}.')
            bakery_is_closed = True
            break

if not bakery_is_closed:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
