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

    encrypted_file_path, decryption_key = encrypt_file(file_path, encrypted_file_name, key_length)

    insert_file(database, {
        "name": encrypted_file_name,
        "location": encrypted_file_path,
        "encryption_alg": "RSA",
        "key_size": key_length
    })
    return_message = "Your file was successfully encrypted! Here is the Private Key for Decryption:\n" + decryption_key
    return return_message


def check_file_cmd(encrypted_file_name):
    database = get_database()
    if not file_name_exists(database, encrypted_file_name):
        raise Exception("Encrypted file name does not exists!")


def decrypt_cmd(encrypted_file_name, decryption_key):
    database = get_database()
    file_info = get_file_by_name(database, encrypted_file_name)[0]
    file_path = file_info[2]
    key_length = int(file_info[4])
    return_message = "Here is your decrypted file:\n" + decrypt_file(file_path, decryption_key, key_length)
    return return_message


def remove_cmd(encrypted_file_name, decryption_key):
    database = get_database()
    file_info = get_file_by_name(database, encrypted_file_name)[0]
    file_path = file_info[2]
    key_length = int(file_info[4])
    decrypt_file(file_path, decryption_key, key_length)
    delete_file(database, encrypted_file_name)
    return "Your file was successfully removed!"
