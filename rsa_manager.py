"""
This module handles the RSA algorithm features:
-key generation,
-message encryption/decryption;
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys(key_length):
    """
    Generates a pair of public-private keys for RSA algorithm;

    :param key_length: The length of the key for RSA algorithm;
    :return: the pair of generated keys.
    """
    key_pair = RSA.generate(key_length)
    public_key = key_pair.publickey().exportKey().decode()
    private_key = key_pair.exportKey().decode()
    return public_key, private_key


def encrypt(message, key):
    """
    Encrypts a given message, using RSA algorithm;

    :param message: the message to be encrypted;
    :param key: the key used for encryption;
    :return: the encrypted message.
    """
    encryptor = PKCS1_OAEP.new(RSA.importKey(key.encode()))
    encrypted = encryptor.encrypt(message)
    return encrypted


def decrypt(message, key):
    """
    Decrypts a given message, using RSA algorithm;

    :param message: the message to be decrypted;
    :param key: the key used for decryption;
    :return: the decrypted message.
    """
    decryptor = PKCS1_OAEP.new(RSA.importKey(key.encode()))
    decrypted = decryptor.decrypt(message)
    return decrypted.decode()
