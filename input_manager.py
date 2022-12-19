from command_manager import *

COMMAND_LIST = "\nCommand List:\n" \
               "1) encrypt <file_path> <encrypted_file_name> <key_length>\n" \
               "2) decrypt <encrypted_file_name>\n" \
               "3) delete <encrypted_file_name>\n"

UNKNOWN_COMMAND = "Unknown Command!"
FEW_ARGUMENTS = "Too Few Arguments Given!"


def read_input_key():
    print("Enter the private key:")
    private_key = ""
    while True:
        line = input()
        if line == "":
            break
        private_key += line + '\n'

    return private_key


def start_input_loop():
    print("Welcome!")
    while True:
        print(COMMAND_LIST)
        command = input("Enter a command:\n")
        command = command.split()
        try:
            if command[0] == "encrypt":
                if len(command) != 4: raise Exception(FEW_ARGUMENTS)
                print(encrypt_cmd(command[1], command[2], command[3]))
            elif command[0] == "decrypt":
                if len(command) != 2: raise Exception(FEW_ARGUMENTS)
                check_file_cmd(command[1])
                decryption_key = read_input_key()
                print(decrypt_cmd(command[1], decryption_key))
            elif command[0] == "delete":
                if len(command) != 2: raise Exception(FEW_ARGUMENTS)
                check_file_cmd(command[1])
                decryption_key = read_input_key()
                print(remove_cmd(command[1], decryption_key))
            elif command[0] == "exit":
                print("Goodbye!")
                break
            else:
                raise Exception(UNKNOWN_COMMAND)
        except Exception as e:
            print("Error:", e)


start_input_loop()
