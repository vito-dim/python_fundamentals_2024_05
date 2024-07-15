student_information = []

command = input()
while ':' in command:
    current_command = command.split(':')
    current_name = current_command[0]
    current_id = int(current_command[1])
    current_course = current_command[2]
    student_information.append({"name": current_name, "ID": current_id, "course": current_course})

    command = input()

search_course = [letter if '_' not in letter else ' ' for letter in command]
search_course_str = ''.join(search_course)

for student in student_information:
    if search_course_str in student['course']:
        print(f"{student['name']} - {student['ID']}")

# student_information = []
#
# command = input()
# while ':' in command:
#     student_information.append(command)
#
#     command = input()
#
# course_name = ''
# for index in range(len(command)):
#     if command[index] == '_':
#         course_name += ' '
#         continue
#
#     course_name += command[index]
#
# for current_student_info in student_information:
#     if course_name in current_student_info:
#         current_name, current_id, current_course = current_student_info.split(':')
#         print(f"{current_name} - {int(current_id)}")

# students = []
# course_to_search = ''
#
# while True:
#     student_info = input()
#
#     if ':' not in student_info:
#         course_to_search = student_info
#         break
#
#     name, id_, course = student_info.split(':')
#     students.append({'name': name, 'ID': id_, 'course': course})
#
# for student in students:
#     if course_to_search.startswith(student['course'][0:5]):
#         print(f"{student['name']} - {student['ID']}")
