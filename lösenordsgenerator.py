  
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars2 = "1234567890"
chars3 = "!%&/()=#"
import random 
import string
password = ""
password = ""
for c in range (897000):
    password += random.choice(chars)
    password += random.choice(chars1)
    

password = ''.join(random.sample(password,len(password)))
print(password)
print(len(password))