def encrypt(plaintext):
    ciphertext=""
    for char in plaintext:
        ch= (ord(char) - ord('A') + 3) % 26
        ciphertext+=chr(ch + ord('A'))
    return ciphertext

def decrypt(ciphertext):
    plaintext=""
    for char in ciphertext:
        ch=(ord(char) - ord('A') - 3)%26
        plaintext+=chr(ch + ord('A'))
    return plaintext

plaintext = input("Enter plaintext:")
print("After encryption:", end=' ')
ct=encrypt(plaintext.upper())
print(ct)
print("After decryption:", end=' ')
pt=decrypt(ct)
print(pt)


