# lower and upper

s = input("enter a string ")

u = 0

l = 0

for i in s:
    if i.islower():
        l += 1

    elif i.isupper():
        u += 1

print("uppercase letters:", u)

print("lowercase letters", l)