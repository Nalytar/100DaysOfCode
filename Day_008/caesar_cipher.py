from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(cipher_direction, start_text, shift_amount):
    new_text = ""
    shift_amount = shift_amount % 26

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
        else:
            new_text += letter
    print(f"The {cipher_direction}d text is {new_text}.")


print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "decode" and direction != "encode":
        print("Your input for de-/encoding was invalid!")
        continue

    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")
    if not shift.isdigit():
        print("Please type in a whole number/integer")
        continue
    else:
        shift = int(shift)

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    repeat = input("Do you want to go again? Y|n\n").lower()
    if repeat == "n":
        break
