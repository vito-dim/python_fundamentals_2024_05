# initial_energy = int(input())
# energy_left = initial_energy
# win_counter = 0
# is_energy_depleted = False
#
# command = input()
#
# while command != 'End of battle':
#     current_distance = int(command)
#
#     if energy_left < current_distance:
#         is_energy_depleted = True
#         break
#     else:
#         win_counter += 1
#         energy_left -= current_distance
#
#         if win_counter % 3 == 0:
#             energy_left += win_counter
#
#     command = input()
#
# if is_energy_depleted:
#     print(f"Not enough energy! Game ends with {win_counter} won battles and {energy_left} energy")
# else:
#     print(f"Won battles: {win_counter}. Energy left: {energy_left}")

def cs_go(energy: int) -> str:
    win_counter = 0

    while True:
        command = input()

        if command == 'End of battle':
            return f"Won battles: {win_counter}. Energy left: {energy}"

        current_distance = int(command)

        if energy >= current_distance:
            energy -= current_distance
            win_counter += 1

            if win_counter % 3 == 0:
                energy += win_counter
        else:
            return f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy"


initial_energy = int(input())
result = cs_go(initial_energy)
print(result)
