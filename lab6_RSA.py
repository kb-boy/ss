import math

def set_keys():
    p, q = 13, 17
    n = p * q
    phi = (p - 1) * (q - 1)
    e = next(e for e in range(2, phi) if math.gcd(e, phi) == 1)
    d = next(d for d in range(2, phi) if (d * e) % phi == 1)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

def encode(message, public_key):
    return [encrypt(ord(ch), public_key) for ch in message]

def decode(encoded, private_key):
    return ''.join(chr(decrypt(num, private_key)) for num in encoded)

if __name__ == "__main__":
    public_key, private_key = set_keys()
    message = "Text Message"
    encoded = encode(message, public_key)
    print("Original:", message)
    print("Encoded:", encoded)
    print("Decoded:", decode(encoded, private_key))
