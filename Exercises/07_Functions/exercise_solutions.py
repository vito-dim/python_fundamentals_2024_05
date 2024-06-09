# 1
def smallest(some_list: list) -> int:
    return min(some_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest([first_number, second_number, third_number])
print(smallest_number)


# 2
def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


# 3
def all_the_characters(first_char, second_char):
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
result = all_the_characters(first_character, second_character)
print(" ".join(result))


# 4
def odd_even_sums(some_number: str):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = input()
print(odd_even_sums(number))


# 5.1
def is_even(current_number):
    return current_number % 2 == 0


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
final_list = list(filter(is_even, numbers_as_digits))
print(final_list)

# 5.2
numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
is_even = lambda x: x % 2 == 0
final_list = list(filter(is_even, numbers_as_digits))
print(final_list)

# 5.3

print([int(number) for number in input().split() if int(number) % 2 == 0])


# 8
def is_palindrome(some_number_as_string):
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")
for number in numbers_as_string:
    print(is_palindrome(number))


# 10
def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))


# 11
def loading_bar(some_number) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent_as_digit = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent_as_digit}{'.' * (10 - loaded_percent_as_digit)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


# 12

def calculate_factorial(some_number: int) -> int:
    for current_number in range(1, some_number):
        some_number *= current_number
    return some_number


first_number = int(input())
second_number = int(input())
first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
print(f"{first_factorial / second_factorial:.2f}")
