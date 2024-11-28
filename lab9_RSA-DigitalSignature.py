from sympy import mod_inverse
from math import gcd

p, q = 823, 953
n = p * q
phi_n = (p - 1) * (q - 1)

e = next(i for i in range(2, phi_n) if gcd(i, phi_n) == 1)
d = mod_inverse(e, phi_n)

M = "190789"
signature = pow(M, d, n)
verified_message = pow(signature, e, n)

print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")
print(f"Original message: {M}")
print(f"Digital signature: {signature}")
print(f"Verified message: {verified_message}")
print("Signature verified successfully!" if verified_message == M else "Signature verification failed.")