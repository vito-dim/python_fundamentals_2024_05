first_string = input()
seconds_string = input()

while first_string in seconds_string:
    seconds_string = seconds_string.replace(first_string, "")

print(seconds_string)
