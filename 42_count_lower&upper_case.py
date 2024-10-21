#write a python program to mi a string of upper and string
s=input("enter string")
a=0
b=0
for i in s:
    if i.isupper():
        a += 1
    else:
        b += 1

print("upper case count:",a)
print("lower case count:",b)        