# WAPP to remove odd elements from the given list
k=[]
n=int(input("enter size:"))
for i in range (n):
    i=int(input(i))
    k.append(i)
print(k)
for i in k :
    if i%2!=0:
        k.remove(i)
    print(k) 
