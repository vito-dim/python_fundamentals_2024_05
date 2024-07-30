phonebook = {}

command = input()
while not command.isnumeric():
    name, phone = command.split("-")
    phonebook[name] = phone
    command = input()

search_counter = int(command)
for _ in range(search_counter):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
