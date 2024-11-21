import re

p = input("Enter password: ")
x = True

while x:
    # Password length between 6 and 12 characters
    if len(p) < 6 or len(p) > 12:
        print("Password length should be between 6 and 12 characters.")
        break
 
    elif not re.search("[0-9]", p):    
        break

    elif not re.search("[A-Z]", p):
        break

    elif not re.search("[a-z]", p):
        break

    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", p):
        break 

    elif " " in p:       
        break
    
    else:
        print("Valid password")
        x = False
        break

if x:
    print("Not a valid password")
