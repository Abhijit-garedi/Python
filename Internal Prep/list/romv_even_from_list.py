# Program to remove the even from the list 

n = int(input("Enter a number: "))  # No of elements
l = []

for i in range(n):
    value = int(input("Enter value: "))
    l.append(value)

l = [i for i in l if i % 2 != 0]

print(l)