white_gold = [int(index) for index in input().split()]
yellow_gold = [int(index) for index in input().split()]

created_earrings = 0
leftover_gold = 0

for index in range(len(white_gold)):
    current_sum = white_gold[index] + yellow_gold[index]
    if current_sum == 10:
        created_earrings += 1
    elif current_sum > 10:
        while True:
            yellow_gold[index] -= 2
            current_sum = white_gold[index] + yellow_gold[index]
            if current_sum == 10:
                created_earrings += 1
                break
            elif current_sum < 10:
                leftover_gold += current_sum
                break
    elif current_sum < 10:
        leftover_gold += current_sum

earrings_from_leftovers = leftover_gold / 10
created_earrings += int(earrings_from_leftovers)

if created_earrings >= 7:
    print(f"Great success, you created {created_earrings} earrings.")

else:
    earrings_needed = abs(7 - created_earrings)
    print(f"Keep trying, you need {earrings_needed} more earrings.")
