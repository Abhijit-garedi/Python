#program to print nth largest element in the list
l=[]

n=int(input("enter size of the list:"))

for i in range(n):
    i=int(input("enter value:"))
    l.append(i)

print(l)

k=1

for i in range(n):
    print("the nth largest elementn:",n)

l.sort(reverse=True)
print[l[k-1]]

k=k+1    