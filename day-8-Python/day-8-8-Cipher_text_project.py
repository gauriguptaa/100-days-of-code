from art import logo


def encrypt(text_to_encrypt, rotate):
    encrypted_code = ''
    for letter in text_to_encrypt:
        index = (alphabet.index(letter)+rotate) % 26
        encrypted_code += alphabet[index]
    return encrypted_code


def decrypt(cipher_text, rotate):
    decoded_text = ''
    for letter in cipher_text:
        index = (alphabet.index(letter) - rotate) % 26
        decoded_text += alphabet[index]
    return decoded_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v',
            'w', 'x', 'y', 'z']

print(logo)

make_cipher = True

while make_cipher:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direction = input("Type 'encode' to encrypt your text , type 'decode' to decrypt:\n").lower()
    cipher = ''
    if direction == 'encode':
        cipher = encrypt(text, shift)
        print(f"Your encoded string is : {cipher}")
    elif direction == 'decode':
        plain_text = decrypt(text, shift)
        print(f"Your decoded string is : {plain_text}")
    else:
        print("Please Enter the Valid option ( encode / decode )")
    option = input("Continue Making Cipher.. (yes/no)").lower()
    if option == 'yes':
        make_cipher = True
    else:
        make_cipher = False

