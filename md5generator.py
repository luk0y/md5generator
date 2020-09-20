#!/usr/bin/python3

import hashlib


data = input("Enter the string to encrypt it into md5 hash : ")
result = hashlib.md5(data.encode())

print("Md5 encypted string is",result.hexdigest(),"\n")
