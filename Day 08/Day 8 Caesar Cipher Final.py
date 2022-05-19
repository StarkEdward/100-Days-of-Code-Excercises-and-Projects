# Caesar Cipher Final code


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    try:
        if direction == 'encode' or direction == 'decode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            shift = shift % 26

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        result = input("Type 'yes' if you want to try again. Otherwise type 'no'\n").lower()
        if result == 'no':
            print("Good bye!")
            break
    except :
        print("Invalid Input, please re-enter.")
