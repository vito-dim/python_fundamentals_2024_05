messages_count = int(input())

for _ in range(1, messages_count + 1):
    current_message = int(input())
    message_output = ''

    if current_message == 88:
        message_output = 'Hello'

    elif current_message == 86:
        message_output = 'How are you?'

    elif current_message > 88:
        message_output = 'Bye.'

    else:
        message_output = 'GREAT!'

    print(message_output)
