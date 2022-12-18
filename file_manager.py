from standard_rsa import *


def decrypt_file(file, decryption_key):
    decrypted_text = ''
    read_size = 128

    with open(file, 'rb') as f:
        while True:
            file_chunk = f.read(read_size)
            if len(file_chunk) == 0:
                break

            decrypted_text += decrypt(file_chunk, decryption_key)

    return decrypted_text


def encrypt_file(file):
    encryption_key, decryption_key = generate_keys()
    encrypted_text = b''
    read_size = 64

    with open(file, 'rb') as f:
        while True:
            file_chunk = f.read(read_size)
            if len(file_chunk) == 0:
                break

            encrypted_text += encrypt(file_chunk, encryption_key)

    with open(file + "_enc.bin", 'wb') as f:
        f.write(encrypted_text)
    return decryption_key
