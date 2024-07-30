student_information = {}

grades_count = int(input())
for _ in range(grades_count):
    current_student = input()
    current_grade = float(input())
    if current_student not in student_information:
        student_information[current_student] = {'grades': []}
    student_information[current_student]['grades'].append(current_grade)

for student, grades_info in student_information.items():
    grades_count = len(student_information[student]['grades'])
    grades_sum = sum(student_information[student]['grades'])
    average_grade = grades_sum / grades_count
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
