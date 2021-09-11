if __name__ == '__main__':
    recipient_names = open("invited_names.txt").readlines()
    for name in recipient_names:
        name = name.strip("\n")
        send_mail = open(f"Ready_to_send\letter_for_{name}.txt", mode="w")
        with open("starting_letter.txt") as file:
            content = file.readlines()
            content[0] = content[0].replace("name", name)
            content_string = ''.join(content)
            send_mail.write(content_string)
