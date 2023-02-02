import string


def decrypt_message(message, shift):
    shifted_message = ""

    for message_char in message:
        if message_char not in string.ascii_letters:
            shifted_message += message_char
            continue

        if message_char.lower() in string.ascii_lowercase:
            new_index = (
                (string.ascii_lowercase.index(message_char.lower()) + shift) + 26
            ) % 26

        if message_char.lower() == message_char:
            shifted_message += string.ascii_lowercase[new_index]
        else:
            shifted_message += string.ascii_uppercase[new_index]

    return shifted_message
