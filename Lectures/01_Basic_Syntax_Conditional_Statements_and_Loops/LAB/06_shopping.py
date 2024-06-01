budget = int(input())
budget_left = budget
shopping_successful = True

command = input()
while command != 'End':
    money_spent = int(command)
    budget_left -= money_spent

    if budget_left < 0:
        shopping_successful = False
        break

    command = input()

if shopping_successful:
    print('You bought everything needed.')

else:
    print('You went in overdraft!')
