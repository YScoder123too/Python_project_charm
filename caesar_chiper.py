alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x',
             'y', 'z'," "]

direction = input("Type 'encode' to 'encrypt',they 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = (position + shift_amount) % len(alphabets)
        new_letter = alphabets[new_position]#isme ascii value store hai wo check bhi to karni hai isliye
        cipher_text += new_letter#khali variable mai bharte raho bruh
    print(f"encoded message is: {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        plain_text += alphabets[new_position]
    print(f"decoded message is: {plain_text}")

if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)
else:
   print("Enter a valid input ")


