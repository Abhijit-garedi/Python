#wapp to accept mixed case and count upper and lower case characters

def count_case(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char is upper():
            upper_count += 1

        elif char.islower():
            lower_count += 1

            return  upper_count,lower_count        

#accpet input from user

user_input = input("enter a string:")

upper,lower = count_case(user_input)

print(f"uppercae characters : {upper}")

print(f"lowercase characters : {lower}")