# WAPP to check given string is palindorme or not 

s = input("enter value")

s1 = s[::-1]

if s == s1:
    print("palindrome")

else:
    print("not palindrome")

