import hashlib
import random
from sympy import mod_inverse

def key_generation(p, q, g):
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    return x, y

def sign_message(M, p, q, g, x):
    H = int(hashlib.sha256(M.encode("utf-8")).hexdigest(), 16)
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    k_inv = mod_inverse(k, q)
    s = (k_inv * (H + x * r)) % q
    return r, s

def verify_signature(M, r, s, p, q, g, y):
    H = int(hashlib.sha256(M.encode("utf-8")).hexdigest(), 16)
    w = mod_inverse(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

p = 23
q = 11
g = 2

private_key, public_key = key_generation(p, q, g)
message = "Hello, this is a message to sign!"
r, s = sign_message(message, p, q, g, private_key)
is_valid = verify_signature(message, r, s, p, q, g, public_key)

print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print(f"Signature: (r, s) = ({r}, {s})")
print(f"Signature valid: {is_valid}")
