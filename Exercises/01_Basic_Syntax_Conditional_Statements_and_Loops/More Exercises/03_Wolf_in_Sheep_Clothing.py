animals = input()
list_animals = animals.split(', ')
list_length = len(list_animals)

for animal_index in range(0, list_length):
    current_animal = list_animals[animal_index]

    if current_animal.lower() == 'wolf':
        if animal_index == list_length + 1:
            print('Please go away and stop eating my sheep')

        else:
            sheep_index = animal_index + 1
            print(f'Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!')
