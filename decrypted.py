#!/usr/bin/env pyhton 3

import os
from cryptography.fernet import Fernet  

files=[]

for file in os.listdir():
	if file =="hack.py" or file=="thekey.key"or file== "decrypted.py" or file == "README.md":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)



with open("thekey.key","rb") as thekey:
	secretkey= thekey.read()

for file in files:
	with open(file,"rb") as thefile:
		contents= thefile.read()
	contents_decrypted= Fernet(secretkey).decrypt(contents)
	with open (file,"wb") as thefile:
		thefile.write(contents_decrypted)

print("All of your files have been decrypted!")
