# employees_happiness = list(map(int, input().split()))
# happiness_improvement = int(input())
#
# improved_happiness = list(current_employee * happiness_improvement for current_employee in employees_happiness)
# average_happiness = sum(improved_happiness) / len(improved_happiness)
# total_count = len(improved_happiness)
# happy_count = 0
# for happy in improved_happiness:
#     if happy >= average_happiness:
#         happy_count += 1
#
# message = 'happy' if happy_count >= total_count // 2 else 'not happy'
#
# print(f'Score: {happy_count}/{total_count}. Employees are {message}!')

employees_happiness = list(map(int, input().split()))
happiness_improvement = int(input())

improved_happiness = list(current_employee * happiness_improvement for current_employee in employees_happiness)
average_happiness = sum(improved_happiness) / len(improved_happiness)
total_count = len(improved_happiness)
happy_count = sum(num >= average_happiness for num in improved_happiness)
message = 'happy' if happy_count >= total_count // 2 else 'not happy'

print(f'Score: {happy_count}/{total_count}. Employees are {message}!')
