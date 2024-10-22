from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    if len(key) != 8:
        print("Key should be of 8 bits")
        exit()
    
    if type(plaintext) is str : plaintext = plaintext.encode('utf-8')
    plaintext = pad(plaintext, DES.block_size)
    iv = get_random_bytes(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext

def decrypt(ciphertext, key):
    if len(key) != 8:
        print("Key should be of 8 bits")
        exit()
    
    iv = ciphertext [ : DES.block_size]
    ciphertext = ciphertext [ DES.block_size : ]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext ,DES.block_size)

    return plaintext.decode('utf-8')

text = input('Enter message:')
key = b'ABCDEFGH'
e =encrypt(text, key)
print("CipherText: ", e)
d = decrypt(e, key)
print("Plaintext: ", d)