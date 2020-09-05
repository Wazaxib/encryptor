from cryptography.fernet import Fernet
key =  # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = 'encrypted.txt'
output_file = 'decrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
