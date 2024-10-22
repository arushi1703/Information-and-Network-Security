from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    if len(key) not in (16, 24, 32):
        print('Key length should be 16/24/32')
        exit()
    
    if type(plaintext) is str : plaintext = plaintext.encode('utf-8')
    plaintext = pad(plaintext, AES.block_size)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext

def decrypt(ciphertext, key):
    if len(key) not in (16, 24, 32):
        print('Key length should be 16/24/32')
        exit()

    iv = ciphertext[ : AES.block_size]
    ciphertext = ciphertext[AES.block_size : ]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext, AES.block_size)

    return plaintext.decode('utf-8')

text = input("Enter plaintext: ")
key = b'ABCDEFGHIJKLMNOPQRSTUVWX'

e= encrypt(text, key)
print("Ciphertext: ", e)
d= decrypt(e, key)
print("Plaintext: ", d)