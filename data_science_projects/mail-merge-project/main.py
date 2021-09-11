if __name__ == '__main__':
    recipient_names = open("invited_names.txt").readlines()
    for name in recipient_names:
        name = name.strip("\n")
        send_mail = open(f"Ready_to_send\letter_for_{name}.txt", mode="w")
        with open("starting_letter.txt") as file:
            content = file.read()
            content = content.replace("name", name)
            send_mail.write(content)
