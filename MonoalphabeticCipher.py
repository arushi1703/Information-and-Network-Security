def encrypt(plaintext,key):
    ciphertext=""
    for char in plaintext:
        ch= (ord(char) - ord('A') + key) % 26
        ciphertext+=chr(ch + ord('A'))
    return ciphertext

def decrypt(ciphertext,key):
    plaintext=""
    for char in ciphertext:
        ch=(ord(char) - ord('A') - key)%26
        plaintext+=chr(ch + ord('A'))
    return plaintext

key=int(input("Enter key:"))
if key>26:
    key=key%26
plaintext = input("Enter plaintext:")
print("After encryption:", end=' ')
ct=encrypt(plaintext.upper(),key)
print(ct)
print("After decryption:", end=' ')
pt=decrypt(ct,key)
print(pt)


