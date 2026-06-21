from cryptography.fernet import Fernet
import base64
import hashlib
import os

print("\n Set your password for Password Manager \n This will create a files called 'secret_text' where your encypted passwords will stored")

while True:

    password = input("\n Enter Password: ")
    re_password = input("\n Enter Password Confirm: ")

    if re_password != password:
        print("\n Please make sure your password matches confirm password \n")

    elif len(password) < 8:
        print("\n Please make sure your password is atleast 8 characters long \n")    
    
    else:
        break


key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()[0:32])
fernet = Fernet(key) 

if not os.path.exists("secret_text.txt"):

    with open("secret_text.txt", "w") as f:
        f.write("Write Your Passwords Here")

    with open("secret_text.txt", "r") as f:
        d1 = f.read().encode()

    with open("secret_text.txt", "wb") as f:
        f.write(fernet.encrypt(d1))

else:
    print("\n FAILED:  A 'secret_text' file already exists \n")