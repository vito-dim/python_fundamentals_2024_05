centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)  # 365.2422 - assumption days on average (the Tropical year).
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
