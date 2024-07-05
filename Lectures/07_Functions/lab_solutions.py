# absolute_values.py
numbers = input().split()

absolute_values = []

for num in numbers:
    absolute_values.append(abs(float(num)))

print(absolute_values)

# calculation.py
# "multiply", "divide", "add", and "subtract".

def calculate_result(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtract': num1 - num2,
    }.get(operator, 'Invalid operator!')


operator = input('Enter the operator (multiply, divide, add, subtract): ')
first_number = int(input('Enter the first value: '))
second_number = int(input('Enter the second value: '))
result = calculate_result(operator, first_number, second_number)
print(result)

# example_file_1.py

nums = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda num: num % 2 == 0, nums))

print(even_numbers)

# functions
# [
#     {
#         "id": 5,
#         "description": "Write documentation",
#         "priority": "medium",
#         "deadline": "2024-06-18",
#         "completed": false
#     },
#     {
#         "id": 6,
#         "description": "Deploy application",
#         "priority": "high",
#         "deadline": "2024-06-17",
#         "completed": false
#     }
# ]

# grades.py
# 2.00 – 2.99 - "Fail"
# 3.00 – 3.49 - "Poor"
# 3.50 – 4.49 - "Good"
# 4.50 – 5.49 - "Very Good"
# 5.50 – 6.00 - "Excellent"

def convert_grade_to_word(grade):
    if 2.00 <= grade <= 2.99:
        return 'Fail'
    elif 3.00 <= grade <= 3.49:
        return 'Poor'
    elif 3.50 <= grade <= 4.49:
        return 'Good'
    elif 4.50 <= grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade <= 6.00:
        return 'Excellent'


grade = float(input())
result = convert_grade_to_word(grade)
print(result)

# repeat_string.py
repeat_string = lambda string, num: string * num

input_string = input()
counter = int(input())
result = repeat_string(input_string, counter)
print(result)