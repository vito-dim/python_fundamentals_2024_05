courses = {}
data = input()
while ':' in data:
    student_name, student_id, course = data.split(':')
    if course not in courses:
        courses[course] = {student_name: student_id}
    else:
        courses[course][student_name] = student_id
    data = input()

course_taken = data.replace('_', ' ')
students = courses[course_taken]

for name, _id in students.items():
    print(f"{name} - {_id}")

# data = input()
# student_information = {}
#
# while ':' in data:
#     student_name, student_id, student_course = data.split(':')
#     student_id = int(student_id)
#
#     if student_course not in student_information:
#         student_information[student_course] = {}
#     student_information[student_course][student_name] = student_id
#
#     data = input()
#
# # course_taken = ' '.join(data.split('_'))
# course_taken = data.replace('_', ' ')
#
# if course_taken in student_information:
#     for name, student_id in student_information[course_taken].items():
#         print(f"{name} - {student_id}")

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
