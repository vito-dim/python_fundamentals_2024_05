people_queue = int(input())
lift_state = [int(current_state) for current_state in input().split(' ')]
lift_limit = 4

for index in range(len(lift_state)):
    people_in_current_state = lift_state[index]

    if people_queue > 3:
        people_entered_lift = abs(lift_limit - people_in_current_state)
        people_queue -= people_entered_lift
        lift_state[index] += people_entered_lift

    else:
        lift_state[index] += people_queue
        people_queue = 0


if people_queue > 0:
    print(f"There isn't enough space! {people_queue} people in a queue!")
elif sum(lift_state) != len(lift_state) * 4:
    print(f"The lift has empty spots!")

print(' '.join(str(num) for num in lift_state))
