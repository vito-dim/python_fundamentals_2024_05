pieces_count = int(input())
pieces_db = {}
for _ in range(pieces_count):
    piece_details = input().split("|")
    current_piece, current_composer, current_key = piece_details
    if current_piece not in pieces_db.keys():
        pieces_db[current_piece] = {"composer": current_composer, "key": current_key}

command = input()
while command != "Stop":
    current_command = command.split("|")

    if "Add" in current_command:
        current_piece, current_composer, current_key = current_command[1], current_command[2], current_command[3]
        if current_piece not in pieces_db:
            pieces_db[current_piece] = {"composer": current_composer, "key": current_key}
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")

    elif "Remove" in current_command:
        current_piece = current_command[1]
        if current_piece in pieces_db:
            del pieces_db[current_piece]
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    elif "ChangeKey" in current_command:
        current_piece, current_key = current_command[1], current_command[2]
        if current_piece in pieces_db:
            pieces_db[current_piece]["key"] = current_key
            print(f"Changed the key of {current_piece} to {current_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    command = input()

for piece, information in pieces_db.items():
    print(f"{piece} -> Composer: {information['composer']}, Key: {information['key']}")
    
    
    
# pieces_count = int(input())
# pieces_db = {}
# for _ in range(pieces_count):
#     piece_details = input().split("|")
#     current_piece, current_composer, current_key = piece_details
#     if current_piece not in pieces_db.keys():
#         pieces_db[current_piece] = {"composer": current_composer, "key": current_key}

# command = input()
# while command != "Stop":
#     current_command = command.split("|")

#     if "Add" in current_command:
#         current_piece, current_composer, current_key = current_command[1], current_command[2], current_command[3]
#         if current_piece not in pieces_db:
#             pieces_db[current_piece] = {"composer": current_composer, "key": current_key}
#             print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
#         else:
#             print(f"{current_piece} is already in the collection!")

#     elif "Remove" in current_command:
#         current_piece = current_command[1]
#         if current_piece in pieces_db:
#             del pieces_db[current_piece]
#             print(f"Successfully removed {current_piece}!")
#         else:
#             print(f"Invalid operation! {current_piece} does not exist in the collection.")

#     elif "ChangeKey" in current_command:
#         current_piece, current_key = current_command[1], current_command[2]
#         if current_piece in pieces_db:
#             pieces_db[current_piece]["key"] = current_key
#             print(f"Changed the key of {current_piece} to {current_key}!")
#         else:
#             print(f"Invalid operation! {current_piece} does not exist in the collection.")

#     command = input()

# for piece in pieces_db.keys():
#     print(f"{piece} -> Composer: {pieces_db[piece]['composer']}, Key: {pieces_db[piece]['key']}")
