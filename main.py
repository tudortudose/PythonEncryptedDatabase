from file_manager import *
from utils import *

print(encrypt_file("file.txt"))
dec_key = read_input_key()
print(decrypt_file("file.txt_enc.bin", dec_key))
