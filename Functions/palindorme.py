# simplest program to find whether given number is palindarome or not 

  
num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
