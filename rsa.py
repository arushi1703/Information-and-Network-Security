def gcd(a,b):
    if a==0 : return b
    return gcd(b%a, a)

def generateKeys(p, q):
    n = p+q
    totient = (p-1)*(q-1)

    for i in range(2, totient):
        if gcd(i, totient) == 1:
            public = i
            break
    
    for k in range(10):
        private = ( 1 + (k*totient)) / public 
        if private != public and private == round(private): break

    return (public, round(private))

def encrypt(m, e, n): return ((m**e)%n)
def decrypt(e, d, n): return ((e**d)%n)

p = int(input("Enter p:"))
q = int(input("Enter q:"))
n = p*q
plaintext = int(input("Enter message:"))
e,d = generateKeys(p, q)

encrypted = encrypt(plaintext, e, n)
decrypted = decrypt(encrypted, d, n)
print(f"Public key  : {e}")
print(f"Private Key: {d}")
print("Encrpted message: ", encrypted)
print("Decrypted message: ", decrypted)
