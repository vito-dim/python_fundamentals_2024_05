animals = input()
list_animals = animals.split(', ')
list_length = len(list_animals)
is_wolf_close = False
sheep_position = 0

for animal_index in range(list_length):
    current_animal = list_animals[animal_index]

    if current_animal.lower() == 'wolf':
        if animal_index == (list_length - 1):
            is_wolf_close = True
        else:
            wolf_position = (list_length - animal_index)
            sheep_position = wolf_position - 1

if is_wolf_close:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!')
