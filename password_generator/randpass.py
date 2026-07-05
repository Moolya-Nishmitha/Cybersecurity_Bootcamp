import random
import string
length = int(input("Enter password length :"))
spec = input("include special characters? (y/n): ")

characters = ""
characters += string.ascii_lowercase
characters += string.ascii_uppercase
characters += string.digits 
    
if spec == "y":
    characters += string.punctuation 


password = ""
for i in range(length):
    password += random.choice(characters)
print(password)


    
    


