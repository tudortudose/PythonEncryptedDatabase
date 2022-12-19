"""
This module handles the file encryption/decryption,
using the RSA block crypto-system.
"""
import os

from rsa_manager import *

ENCRYPTED_FILES_DIR = "C:\\Users\\tudor\\Desktop\\Faculty\\Year_3\\Sem_1\\PP\\GitProjects\\" \
                      "PythonEncryptedDatabase\\encrypted_files"


def decrypt_file(file, decryption_key, key_length):
    """
    Decrypts the given file content using RSA block decryption.

    :param file: the file to be decrypted;
    :param decryption_key: the decryption key;
    :param key_length: the length of the decryption key;
    :return: The decrypted content of the given file.
    """
    decrypted_text = ''
    read_size = key_length // 8

    with open(file, 'rb') as f:
        while True:
            file_chunk = f.read(read_size)
            if len(file_chunk) == 0:
                break

            decrypted_text += decrypt(file_chunk, decryption_key)

    return decrypted_text


def encrypt_file(file, encrypted_file_name, key_length):
    """
    Encrypts the given file content using RSA block encryption;

    :param file: the file to be encrypted;
    :param encrypted_file_name: the name of the encrypted file;
    :param key_length: the length of the encryption key;
    :return: the path of the encrypted file and the decryption key.
    """
    encryption_key, decryption_key = generate_keys(key_length)
    encrypted_text = b''
    read_size = key_length // 16

    with open(file, 'rb') as f:
        while True:
            file_chunk = f.read(read_size)
            if len(file_chunk) == 0:
                break

            encrypted_text += encrypt(file_chunk, encryption_key)

    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, encrypted_file_name)
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_text)
    return encrypted_file_path, decryption_key
