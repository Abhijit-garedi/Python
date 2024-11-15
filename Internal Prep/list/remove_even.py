#remove even from the list 
n = int(input("enter size "))

l = []

for i in range(n):
    i = int(input("enter values"))
    l.append[i]

print(l)
temp = [0]
l[0] = l[-1]
l[-1] = temp
print(l)    