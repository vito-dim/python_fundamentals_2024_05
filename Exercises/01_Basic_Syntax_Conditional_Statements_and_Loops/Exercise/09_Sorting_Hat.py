current_name = input()

is_name_spoken = False

while current_name != 'Welcome!':
    if current_name == 'Voldemort':
        is_name_spoken = True
        break

    if len(current_name) < 5:
        print(f'{current_name} goes to Gryffindor.')
    elif len(current_name) == 5:
        print(f'{current_name} goes to Slytherin.')
    elif len(current_name) == 6:
        print(f'{current_name} goes to Ravenclaw.')
    else:  # elif len(current_name) > 6:
        print(f'{current_name} goes to Hufflepuff.')

    current_name = input()

if is_name_spoken:
    print('You must not speak of that name!')
else:
    print('Welcome to Hogwarts.')
