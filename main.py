from standard_rsa import *

message = "This is my message!"

encryption_key, decryption_key = generate_keys()
encrypted_text = encrypt(message, encryption_key)
decrypted_text = decrypt(encrypted_text, decryption_key)

print("Original Message:", message)
print("Encrypted message:", encrypted_text)
print("Decrypted message:", decrypted_text)
