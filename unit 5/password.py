import re

def verify_password(password):
    
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    return "Password is valid!"

password = input("Enter a password: ")
print(verify_password(password))
