from math import gcd
from sympy import mod_inverse

def encrypt(message, e,n):
    return pow(message, e, n)

def decrypt(cipher, d,n):
    return pow(cipher, d, n)

def encode(message, public_key,n):
    return [encrypt(ord(ch), public_key,n) for ch in message]

def decode(encoded, private_key,n):
    return ''.join(chr(decrypt(num, private_key,n)) for num in encoded)

p, q = 13, 17
n = p * q
phi = (p - 1) * (q - 1)
e = next(e for e in range(2, phi) if gcd(e, phi) == 1)
d = mod_inverse(e, phi)
message = "Text Message"
encoded = encode(message, e, n)
decoded = decode(encoded, d, n)

print("Original:", message)
print("Encoded:", encoded)
print("Decoded:", decoded)