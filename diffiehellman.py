def getAlpha(q):
    for a in range(q):
        valid = True
        values = set()

        for i in range(1, q): values.add((a ** i) % q)

        for i in range(1, q):
            if i not in values:
                valid = False
                break
      
        if valid:
            alpha = a
            break
    return alpha

def generatePublic(private, alpha, q) : return (alpha**private)%q

def generateShared(public, private, q): return (public**private)%q

q = int(input("Enter value for q: "))
aPrivate = int(input("Enter private key of A: "))
bPrivate = int(input("Enter private key of B: "))
alpha = getAlpha(q)
print("Alpha: ", alpha)
aPublic = generatePublic(aPrivate, alpha, q)
bPublic = generatePublic(bPrivate, alpha, q)
print(f"A: , {(aPublic, aPrivate)}")
print(f"B: , {(bPublic, bPrivate)}")
aShared = generateShared(aPublic, bPrivate, q)
bShared = generateShared(bPublic, aPrivate, q)
print(f"A Shared key : {aShared}")
print(f"B Shared key: {bShared}")
