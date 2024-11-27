import hashlib

def sha1_hash(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode("utf-8"))
    return sha1.hexdigest()

input_str = input("Enter a string to hash: ")
hash_value = sha1_hash(input_str)
print(f"SHA-1 hash of '{input_str}': {hash_value}")