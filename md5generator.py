#python code for generating md5 hash
import hashlib
data=input("\nEnter the string to encrypt it into md5 hash : ") 
result = hashlib.md5(data.encode())
print("\nmd5 encypted string is",result.hexdigest(),"\n")
