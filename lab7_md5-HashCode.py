import hashlib

def md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()

user_input = input("Enter a string to hash with MD5: ")
hash_result = md5_hash(user_input)
print(f"MD5 hash of '{user_input}': {hash_result}")