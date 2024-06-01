number = float(input())
number_type = ""

if number > 0:
    number_type = "positive"
    if abs(number) < 1:
        number_type = "small " + number_type
    elif abs(number) > 1_000_000:
        number_type = "large " + number_type

elif number < 0:
    number_type = "negative"
    if abs(number) < 1:
        number_type = "small " + number_type
    elif abs(number) > 1_000_000:
        number_type = "large " + number_type

else:
    number_type = "zero"

print(number_type)
