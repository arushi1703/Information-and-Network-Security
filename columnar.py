import math

def getSequence(key):
    letters = list(key)
    positions=[]
    for i in range(len(key)):
        positions.append((letters[i], i))
    positions =sorted(positions)

    sequence = [0 for _ in range(len(key))]
    for i in range(len(positions)):
        letter, original = positions[i]
        sequence[original] = i

    column_sequence=[]
    for i in range(len(sequence)):
        column_sequence.append((sequence[i], i))
    column_sequence.sort()
    return column_sequence

def encrypt(plaintext, key):
    ciphertext=''
    sequence = getSequence(key)
    rows = math.ceil(len(plaintext)/len(key))
    cols = len(key)
    matrix= [['_' for j in range(cols)]for i in range(rows)]

    ptr=0
    for row in range(rows):
        for col in range(cols):
            if ptr<len(plaintext):
                matrix[row][col] = plaintext[ptr] if plaintext[ptr] != ' ' else '_'
                ptr+=1
            else: matrix[row][col] = '_'
    
    for _, col in sequence:
        for row in range(rows):
            ciphertext += matrix[row][col]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext=''
    sequence = getSequence(key)
    rows = math.ceil(len(plaintext)/len(key))
    cols = len(key)
    matrix= [['_' for j in range(cols)]for i in range(rows)]

    ptr=0
    for _,col in sequence:
        for row in range(rows):
            if ptr<len(ciphertext):
                matrix[row][col] = ciphertext[ptr]
                ptr+=1
            else: matrix[row][col] = '_'
    
    for row in range(rows):
        for col in range(cols):
            plaintext += matrix[row][col] if matrix[row][col] != ' ' else '_'
    return plaintext

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
e = encrypt(text, key)
print("Ciphertext: ", e)
d= decrypt(e, key)
print("Plaintext: ", d)