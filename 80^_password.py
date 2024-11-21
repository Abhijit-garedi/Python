import re

p = input("Enter password: ")
x = True

while x:
    # Password length between 6 and 12 characters
    if len(p) < 6 or len(p) > 12:
        print("Password length should be between 6 and 12 characters.")
        break
    # Must have at least one digit
    elif not re.search("[0-9]", p):
        print("passowrd should contain at least one number")
        
        break
    # Must have at least one uppercase letter
    elif not re.search("[A-Z]", p):
        print("Password must contain at least one uppercase letter.")
        break


    # Must have at least one lowercase letter
    elif not re.search("[a-z]", p):
        print("Password must contain at least one lowercase letter.")
        break


    # Must have at least one special symbol
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", p):
        print("Password must contain at least one special symbol.")
        break

    
    # Should not contain spaces
    elif " " in p:
        print("Password should not contain spaces.")
        break
    else:
        print("Valid password")
        x = False
        break

if x:
    print("Not a valid password")
