def read_input_key():
    print("Enter the private key:")
    private_key = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        private_key += line + '\n'

    return private_key
