number_of_lines = int(input())
total_sum = 0

for _ in range(number_of_lines):
    current_line = input()
    total_sum += ord(current_line)

print(f'The sum equals: {total_sum}')
