import random

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate(length):
    p = 0
    while not is_prime(p):
        p = random.getrandbits(length)
    return p

P = generate_prime_candidate(8) #23
G = random.randint(2, P-1) #6
a = 4
x = pow(G, a, P)
b = 3
y = pow(G, b, P)

ka = pow(y, a, P)
kb = pow(x, b, P)

print("The value of P:", P)
print("The value of G:", G)
print("The private key a for Alice:", a)
print("Alice's public key is:", x)
print("The private key b for Bob:", b)
print("Bob's public key is:", y)
print("Secret key for Alice is:", ka)
print("Secret key for Bob is:", kb)