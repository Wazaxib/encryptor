from cryptography.fernet import Fernet
key =  # Use one of the methods to get a key (it must be the same when decrypting)
input_file = 'gh.txt'
output_file = 'encrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)