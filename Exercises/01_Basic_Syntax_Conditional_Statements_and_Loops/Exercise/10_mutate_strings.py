first_string = input()
second_string = input()

last_string = first_string

for i in range(len(first_string)):
    left_part = second_string[:i + 1]
    right_part = first_string[i + 1:]
    current_new_string = left_part + right_part

    if last_string != current_new_string:
        last_string = current_new_string
        print(last_string)
