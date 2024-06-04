number_of_snowballs = int(input())
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

for ball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality

    if current_value > snowball_value:
        snowball_value = int(current_value)
        snowball_weight = current_weight
        snowball_time = current_time
        snowball_quality = current_quality

print(f'{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})')
