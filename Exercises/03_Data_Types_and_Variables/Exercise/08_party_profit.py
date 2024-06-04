companions_count = int(input())
adventure_days = int(input())
coins_collected = 0

for day in range(1, adventure_days + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    if day % 3 == 0:
        coins_collected -= 3 * companions_count
    if day % 5 == 0:
        coins_collected += 20 * companions_count
        if day % 3 == 0:
            coins_collected -= 2 * companions_count
    coins_collected += 50
    coins_collected -= 2 * companions_count

coins = int(coins_collected / companions_count)

print(f"{companions_count} companions received {coins} coins each.")
