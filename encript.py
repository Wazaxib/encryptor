def encrypt_decrypt(password):
        enc_str = 'id83he7d9jeu29w874b388s8f84j389e8djri39e98rj39'
        return "".join([chr(ord(a) ^ ord(b)) for a,b in zip(password,enc_str)])

file = open ("GH.txt","r")
output = file.read()

file.close()

print(output)


