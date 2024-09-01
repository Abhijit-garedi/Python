# program for findidng student grade using if elif else statement

n = int(input("Enter value: "))
if n > 80:
    print("Distinction")
elif (n > 60) and (n <= 80):
    print("First")
elif (n > 50) and (n <= 60):
    print("Second")
elif (n > 40) and (n <= 50):
    print("Pass")
else:
    print("Fail")
