number_iterations = int(input())
are_even = True

for i in range(number_iterations):
    current_number = int(input())

    if not current_number % 2 == 0:
        print(f'{current_number} is odd!')
        are_even = False
        break

if are_even:
    print('All numbers are even.')
