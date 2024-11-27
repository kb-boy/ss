def power(a, b, p):
    return pow(a, b, p)

P = 23
G = 6
a = 4
x = power(G, a, P)
b = 3
y = power(G, b, P)

ka = power(y, a, P)
kb = power(x, b, P)

print("The value of P:", P)
print("The value of G:", G)
print("The private key a for Alice:", a)
print("Alice's public key is:", x)
print("The private key b for Bob:", b)
print("Bob's public key is:", y)
print("Secret key for Alice is:", ka)
print("Secret key for Bob is:", kb)
