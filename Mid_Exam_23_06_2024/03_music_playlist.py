list_of_songs = input().split()
commands_count = int(input())

for command in range(commands_count):
    current_command = input()

    if 'Add Song' in current_command:
        new_song = current_command.split(' * ')[1]
        if new_song not in list_of_songs:
            list_of_songs.append(new_song)
            print(f"{new_song} successfully added")

    elif 'Delete Song' in current_command:
        number_of_songs = int(current_command.split(' * ')[1])

        if len(list_of_songs) >= number_of_songs:
            deleted_songs_list = list_of_songs[:number_of_songs]
            list_of_songs = list_of_songs[number_of_songs:]
            print(f"{', '.join(deleted_songs_list)} deleted")

    elif 'Shuffle Songs' in current_command:
        command_attributes = current_command.split(' * ')
        first_song_index = int(command_attributes[1])
        second_song_index = int(command_attributes[2])

        if first_song_index in range(len(list_of_songs)) and second_song_index in range(len(list_of_songs)):
            list_of_songs[first_song_index], list_of_songs[second_song_index] = list_of_songs[second_song_index], \
                list_of_songs[first_song_index]
            print(f"{list_of_songs[first_song_index]} is swapped with {list_of_songs[second_song_index]}")

    elif 'Insert' in current_command:
        command_attributes = current_command.split(' * ')
        new_song = command_attributes[1]
        new_song_index = int(command_attributes[2])

        if new_song_index not in range(len(list_of_songs)):
            print("Index out of range")
        elif new_song in list_of_songs:
            print("Song is already in the playlist")
        else:
            list_of_songs.insert(new_song_index, new_song)
            print(f"{new_song} successfully inserted")

    elif current_command == 'Sort':
        list_of_songs.sort(reverse=True)

    elif current_command == 'Play':
        print("Songs to Play:")
        for song in list_of_songs:
            print(song)
