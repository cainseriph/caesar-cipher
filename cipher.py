
#Collect Input
key = int(input("Please enter the number of places to shift: "))
plaintext = input("Please enter a sentence: ")

# Encryption
ciphertext = ""
for char in plaintext:
    if char.isalpha():
        shift = ord(char) + key
        if char.isupper():
            if shift > ord('Z'):
                shift -= 26
            ciphertext += chr(shift)
        else:
            if shift > ord('z'):
                shift -= 26
            ciphertext += chr(shift)
    else:
        ciphertext += char

print("Encrypted text:", ciphertext)

# Decryption
decrypted_text = ""
for char in ciphertext:
    if char.isalpha():
        shift = ord(char) - key
        if char.isupper():
            if shift < ord('A'):
                shift += 26
            decrypted_text += chr(shift)
        else:
            if shift < ord('a'):
                shift += 26
            decrypted_text += chr(shift)
    else:
        decrypted_text += char

print("Decrypted text:", decrypted_text)
