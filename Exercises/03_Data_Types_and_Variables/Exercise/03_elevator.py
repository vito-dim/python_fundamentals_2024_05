from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())

courses = ceil(number_of_people / elevator_capacity)

print(courses)

# people = int(input())
# capacity = int(input())
# courses = 0
#
# if people <= capacity:
#     courses += 1
#
# else:
#     full_courses = people // capacity
#     people_left = people % capacity
#
#     if people_left != 0:
#         courses += full_courses + 1
#     else:
#         courses += full_courses
#
# print(courses)

# people = int(input())
# capacity = int(input())
# courses = 0
#
# full_courses = people // capacity
# people_left = people % capacity
#
# if people_left != 0:
#     courses += full_courses + 1
# else:
#     courses += full_courses
#
# print(courses)
