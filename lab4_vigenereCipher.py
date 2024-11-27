def generate_key(plaintext, keyword):
    keyword = keyword.upper()
    return "".join(keyword[i % len(keyword)] if char.isalpha() else char for i, char in enumerate(plaintext))

def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, keyword)
    return "".join(
        chr((ord(p) - ord("A") + ord(k) - ord("A")) % 26 + ord("A")) if p.isalpha() else p
        for p, k in zip(plaintext, key)
    )

def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, keyword)
    return "".join(
        chr((ord(c) - ord("A") - (ord(k) - ord("A"))) % 26 + ord("A")) if c.isalpha() else c
        for c, k in zip(ciphertext, key)
    )

# Predefined inputs
plaintext = "Hello, World!"
keyword = "KEY"

# Encryption and decryption
encrypted_text = vigenere_encrypt(plaintext, keyword)
decrypted_text = vigenere_decrypt(encrypted_text, keyword)

# Output results
print(f"Plaintext: {plaintext}")
print(f"Keyword: {keyword}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
