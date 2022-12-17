from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys():
    key_pair = RSA.generate(1024)
    public_key = key_pair.publickey().exportKey().decode()
    private_key = key_pair.exportKey().decode()
    return public_key, private_key


def encrypt(message, key):
    encryptor = PKCS1_OAEP.new(RSA.importKey(key.encode()))
    encrypted = encryptor.encrypt(message.encode())
    return encrypted


def decrypt(message, key):
    decryptor = PKCS1_OAEP.new(RSA.importKey(key.encode()))
    decrypted = decryptor.decrypt(message)
    return decrypted.decode()
