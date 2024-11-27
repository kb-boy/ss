import string


def generate_key_matrix(key):
    alphabet = string.ascii_uppercase.replace("J", "")
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))
    matrix = [list(key[i : i + 5]) for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j
    return None


def process_pairs(text):
    text = text.upper().replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            b = text[i + 1]
            i += 2
        else:
            b = "X" if a != "X" else "Z"
            i += 1
        pairs.append((a, b))
    if len(pairs) > 0 and len(pairs[-1]) == 1:
        pairs[-1] = (pairs[-1][0], "X")
    return pairs


def playfair_encrypt(key, plaintext):
    matrix = generate_key_matrix(key)
    pairs = process_pairs(plaintext)
    ciphertext = []

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

    return "".join(ciphertext)


def playfair_decrypt(key, ciphertext):
    matrix = generate_key_matrix(key)
    pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]
    plaintext = []

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])

    return "".join(plaintext)


key = "KEYWORD"
plaintext = "HELLO WORLD"
encrypted_text = playfair_encrypt(key, plaintext.replace(" ", ""))
decrypted_text = playfair_decrypt(key, encrypted_text)

print("Key Matrix:")
matrix = generate_key_matrix(key)
for row in matrix:
    print(row)

print(f"\nPlaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
