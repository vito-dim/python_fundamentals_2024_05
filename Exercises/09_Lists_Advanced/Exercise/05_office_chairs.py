rooms_count = int(input())
total_free_chairs = 0
enough_chairs = True

for room in range(1, rooms_count + 1):
    chairs_and_visitors_information = input().split()
    chairs_count = chairs_and_visitors_information[0].count('X')
    visitors = int(chairs_and_visitors_information[1])
    if chairs_count < visitors:
        enough_chairs = False
        needed_chairs_in_room = visitors - chairs_count
        print(f'{needed_chairs_in_room} more chairs needed in room {room}')
    else:
        total_free_chairs += (chairs_count - visitors)

if enough_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
