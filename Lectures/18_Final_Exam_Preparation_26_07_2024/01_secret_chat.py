def insert_space(text: str, insert_index: int) -> str:
    left_side = text[:index]
    right_side = text[index:]
    result = left_side + " " + right_side
    return result


def reverse_string(text: str, str_to_replace: str) -> str:
    if str_to_replace in text:
        text = text.replace(str_to_replace, "", 1)
        reversed_replacement = str_to_replace[::-1]
        result = text + reversed_replacement
        return result
    return "error"


def change_all(text: str, sub_str: str, replace_str: str) -> str:
    result = text.replace(sub_str, replace_str)
    return result


encoded_message = input()
command = input()
while command != "Reveal":
    current_command = command.split(":|:")
    if "InsertSpace" in current_command:
        index = int(current_command[1])
        encoded_message = insert_space(encoded_message, index)
        print(encoded_message)
    elif "Reverse" in current_command:
        substring = current_command[1]
        reverse_substring = reverse_string(encoded_message, substring)
        if reverse_substring != "error":
            encoded_message = reverse_substring
            print(encoded_message)
        else:
            print("error")
    elif "ChangeAll" in current_command:
        substring = current_command[1]
        replacement = current_command[2]
        encoded_message = change_all(encoded_message, substring, replacement)
        print(encoded_message)

    command = input()

print(f"You have a new text message: {encoded_message}")
