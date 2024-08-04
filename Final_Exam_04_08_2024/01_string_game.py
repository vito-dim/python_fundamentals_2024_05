text = input()

command = input().split()
while "Done" not in command:
    if "Change" == command[0]:
        char_to_replace = command[1]
        replacement_char = command[2]
        text = text.replace(char_to_replace, replacement_char)
        print(text)

    elif "Includes" == command[0]:
        sub_string = command[1]
        check_if_included = sub_string in text
        print(check_if_included)

    elif "End" == command[0]:
        sub_string = command[1]
        check_if_endswith = text.endswith(sub_string)
        print(check_if_endswith)

    elif "Uppercase" == command[0]:
        text = text.upper()
        print(text)

    elif "FindIndex" == command[0]:
        char_to_find = command[1]
        index_found = text.index(char_to_find)
        print(index_found)

    elif "Cut" == command[0]:
        start_index = int(command[1])
        count = int(command[2])
        left_part = text[start_index:]
        part_to_remove = left_part[count:]
        cut_result = left_part.replace(part_to_remove, "")
        print(cut_result)

    command = input().split()
