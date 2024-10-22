def getKey(keyword):
    key = keyword.upper().replace('J', 'I')
    result=''
    for char in key:
        if char not in result:
            result+=char
    return result

def getMatrix(keyword):
    key = getKey(keyword)
    grid = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyset = set(key)

    for char in key:
        grid.append(char)

    for char in alphabet:
        if char not in keyset:
            grid.append(char)
    
    if 'X' not in grid:
        grid.append('X')  # Optionally insert 'X'

    matrix = [ grid[i:i+5] for i in range(0,25,5)]
    return matrix

def getPairs(text):
    text =text.upper().replace('J', 'I')
    i = 0
    pairs=[]

    while i < len(text):
        a = text[i]
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                pairs.append(a+'X')
                i+=1
            else:
                pairs.append(a+b)
                i+=2
        else : 
            pairs.append(a+'X')
            i+=1
    return pairs

def getPositions(matrix):
    positions={}
    for i in range(5):
        for j in range(5):
            positions[matrix[i][j]] = (i, j)
    return positions

def encrypt(plaintext, key):
    matrix = getMatrix(key)
    pairs = getPairs(plaintext)
    positions = getPositions(matrix)
    ciphertext =""

    for pair in pairs:
        row1, col1 = positions[pair[0]]
        row2, col2 = positions[pair[1]]

        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def decrypt(ciphertext, key):
    matrix = getMatrix(key)
    pairs = getPairs(ciphertext)
    positions = getPositions(matrix)
    plaintext =""

    for pair in pairs:
        row1, col1 = positions[pair[0]]
        row2, col2 = positions[pair[1]]

        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

text = input("Enter text:")
key = input("Enter key:")
e=  encrypt(text, key)
print("Ciphertext: ", e)
d= decrypt(e, key)
print("Plaintext: ", d)