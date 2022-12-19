from mysql_manager import *
from file_manager import *


def encrypt_cmd(file_path, encrypted_file_name, key_length):
    is_file = os.path.isfile(file_path)
    if not is_file:
        raise Exception("Incorrect file path!")

    database = get_database()
    if file_name_exists(database, encrypted_file_name):
        raise Exception("Encrypted file name already exists!")

    for ch in key_length:
        if not ('0' <= ch <= '9'):
            raise Exception("Key length should be an integer, multiple of 1024")

    key_length = int(key_length)
    if key_length % 1024 != 0:
        raise Exception("Key length should be a multiple of 1024")

    encrypted_file_path, decryption_key = encrypt_file(file_path, encrypted_file_name)

    insert_file(database, {
        "name": encrypted_file_name,
        "location": encrypted_file_path,
        "encryption_alg": "RSA",
        "key_size": key_length
    })
    return decryption_key


def check_file_cmd(encrypted_file_name):
    database = get_database()
    if not file_name_exists(database, encrypted_file_name):
        raise Exception("Encrypted file name does not exists!")


def decrypt_cmd(encrypted_file_name, decryption_key):
    database = get_database()
    file_info = get_file_by_name(database, encrypted_file_name)[0]
    file_path = file_info[2]
    return decrypt_file(file_path, decryption_key)


def remove_cmd(encrypted_file_name, decryption_key):
    database = get_database()
    file_info = get_file_by_name(database, encrypted_file_name)[0]
    file_path = file_info[2]
    decrypt_file(file_path, decryption_key)
    delete_file(database, encrypted_file_name)
    return "Successfully removed!"
