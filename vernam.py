def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        letter1 = ord(plaintext[i]) - ord('A')
        letter2 = ord(key[i]) - ord('A')
        newletter = letter1 + letter2
        if newletter >= 26 : newletter -= 26
        ciphertext += chr(newletter + ord('A'))
    return ciphertext

def decrypt(ciphertext, key):
    plaintext= ''
    for i in range(len(ciphertext)):
        letter1 = ord(ciphertext[i]) - ord('A')
        letter2 = ord(key[i]) - ord('A')
        newletter = letter1 - letter2
        if newletter < 0 : newletter +=26
        plaintext += chr(newletter + ord('A'))
    return plaintext 

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

if len(key) != len(text):
    print("Invalid Key")
    exit()

ct = encrypt(text , key)
pt = decrypt(ct, key)
print("Ciphertext: ", ct)
print("Plaintext: ", pt)