# ascii_values.py
char_dict = {char: ord(char) for char in input().split(', ')}
print(char_dict)

# bakery.py
data = input().split()

stock = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])
    stock[food] = quantity

print(stock)

# example_1.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squares)

# statistics.py
stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

product_count = len(stock)
total_quantity = sum(stock.values())

print(f'Products in stock:')
for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_quantity}')

# stock.py
stock_data = input().split()

stock = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = int(stock_data[i + 1])
    stock[product] = quantity

product_to_search = input().split()

for product in product_to_search:
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')

# students.py
students = []
course_to_search = ''

while True:
    student_info = input()

    if ':' not in student_info:
        course_to_search = student_info
        break

    name, id_, course = student_info.split(':')
    students.append({'name': name, 'ID': id_, 'course': course})

for student in students:
    if course_to_search.startswith(student['course'][0:5]):
        print(f"{student['name']} - {student['ID']}")

# word_synonyms.py
n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym_list in synonyms.items():
    synonym_str = ', '.join(synonym_list)
    print(f'{word} - {synonym_str}')