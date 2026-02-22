#WAPP to print nth largest element in the list

l=[]
n=int(input("enter size"))
for i in range(n):
    k=int(input("enter value"))
    l.append(i)
print(l)
l.sort
l.reverse()
print(l)
t=int(input("enter n largest"))
if t<n :
    print("{} is in place {}" . format(t,l[t-1]))
