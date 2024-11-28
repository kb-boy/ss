import numpy as np

def mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  # Calculate determinant
    det_inv = pow(det, -1, modulus)          # Modular inverse of determinant
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)  # Adjugate matrix
    return (det_inv * adjugate) % modulus    # Modular inverse of matrix

def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    text_values = [ord(char) - ord("A") for char in text]
    # Add padding if necessary
    padding = (size - len(text_values) % size) % size
    text_values += [ord("X") - ord("A")] * padding
    return np.array(text_values).reshape(-1, size), padding

def matrix_to_text(matrix):
    return ''.join(
        chr((value % 26) + ord("A"))
        for row in matrix
        for value in row
    )

def hill_encrypt(key, plaintext):
    plaintext_matrix, _ = text_to_matrix(plaintext, len(key))
    encrypted_matrix = np.dot(plaintext_matrix, key) % 26
    return matrix_to_text(encrypted_matrix)

def hill_decrypt(key, ciphertext, padding):
    ciphertext_matrix, _ = text_to_matrix(ciphertext, len(key))
    key_inverse = mod_inverse(key, 26)
    decrypted_matrix = np.dot(ciphertext_matrix, key_inverse) % 26
    decrypted_text = matrix_to_text(decrypted_matrix)
    return decrypted_text[:-padding] if padding > 0 else decrypted_text

# Example usage
key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plaintext = "Hello World"

ciphertext = hill_encrypt(key, plaintext)
plaintext_matrix, padding = text_to_matrix(plaintext, len(key))
decrypted_text = hill_decrypt(key, ciphertext, padding)

print("\nKey Matrix:")
print(key)
print(f"\nPlaintext: {plaintext}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
