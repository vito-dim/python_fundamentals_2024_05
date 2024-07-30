parking_db = {}

commands_count = int(input())
for _ in range(commands_count):
    command = input().split()
    if command[0].startswith('register'):
        username = command[1]
        license_plate_number = command[2]
        if username not in parking_db:
            parking_db[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0].startswith('unregister'):
        username = command[1]
        if username not in parking_db:
            print(f"ERROR: user {username} not found")
        else:
            del parking_db[username]
            # parking_db.pop(username)
            print(f"{username} unregistered successfully")

for name, plate_number in parking_db.items():
    print(f"{name} => {plate_number}")
