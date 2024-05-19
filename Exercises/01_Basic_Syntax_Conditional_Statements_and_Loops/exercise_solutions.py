#1

name = input()
if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")

#2
ages = int(input())
drink = ""
if ages <= 14:
    drink = "toddy"
elif ages <= 18:
    drink = "coke"
elif ages <= 21:
    drink = "beer"
else:  # elif ages > 21
    drink = "whisky"
print(f"drink {drink}")


#3
number_of_messages = int(input())
for current_message in range(number_of_messages):
    number = int(input())
    message = ""
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88:
        message = "GREAT!"
    else:  # elif number > 88
        message = "Bye."
    print(message)


#4

divisor = int(input())
boundary = int(input())
for number in range(boundary, divisor-1, -1):
    if number % divisor == 0:
        break
print(number)

#5

number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days not in range(1, 31+1): #elif days < 1 or days > 31:
        continue
    elif capsules_per_day not in range(1, 2000 + 1):#elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")

#6
number_of_string = int(input())
for current_strings in range(number_of_string):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")



#7

current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for character in current_string:
            new_string += character * 2
        print(new_string)
    current_string = input()

#8
coffee_counter = 0
command = input()
while command != "END":
    if command.lower() == "coding" or\
            command.lower() == "dog" or \
            command.lower() == "cat" or \
            command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else: # if commans.isupper():
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

#10

first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string






#12

quantity_of_decorations = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
