alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift):
    encrypted_message = []
    for letter in message:
        if letter in alphabet:
            shifted_index =alphabet.index(letter) + shift
            if shifted_index > len(alphabet)-1:
                shifted_index = shifted_index - len(alphabet)
            encrypted_message.append(alphabet[shifted_index])
        else:
            encrypted_message.append(letter)
    return "".join(encrypted_message)

def decrypt(message,shift):
    decrypted_message = []
    for letter in message:
        if letter in alphabet:
            shifted_index =alphabet.index(letter) - shift
            if shifted_index < 0 :
                shifted_index = len(alphabet) + shifted_index
            decrypted_message.append(alphabet[shifted_index])
        else:
            decrypted_message.append(letter)
    return "".join(decrypted_message)
want_continue = "Y"

while want_continue =="Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction =="encode":
        result = encrypt(text,shift)
        print(f"You encrypted word is: {result}.")
    elif direction =="decode":
        result = decrypt(text,shift)
        print(f"Decrypted message is {result}.")
    else:
        print("Wrong command!")
    want_continue = input("Do you want to continue 'Y' or exit 'N' :\n")