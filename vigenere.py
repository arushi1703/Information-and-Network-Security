def displayMatrix(grid):
    for i in range(26):
        for j in range(26):
            print(grid[i][j], end=' ')
        print()

def getMatrix():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grid = [['_' for j in range(26)] for i in range(26)]

    start=0
    for i in range(26):
        ptr= start
        for j in range(26):
            grid[i][j]= letters[ptr]
            ptr = (ptr+1)%26
        start+=1
    return grid

def padkey(text, key):
    newkey=''
    ptr=0
    for _ in text:
        newkey += key[ptr]
        ptr = (ptr +1)%len(key)
    return newkey

def encrypt(plaintext, key, grid):
    key = padkey(plaintext, key)
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            row = ord(plaintext[i]) - ord('A')
            col = ord(key[i]) - ord('A')
            ciphertext += grid[row][col]
        else : ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, key, grid):
    key = padkey(ciphertext, key)
    plaintext= ""
    for i in range(len(ciphertext)):
        row = ord(key[i]) - ord('A')
        if ciphertext[i].isalpha():
            for j in range(26):
                if grid[row][j] == ciphertext[i]:
                    plaintext += chr(j + ord('A'))
                    break
        else : plaintext+= ciphertext[i]
    return plaintext


text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

if len(key)> len(text):
    print("Invalid key")
    exit()

grid = getMatrix()
e  = encrypt(text, key, grid)
print("Ciphertext: ", e)
d = decrypt(e, key, grid)
print("Plaintext: ", d)