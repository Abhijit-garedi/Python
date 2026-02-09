# WAPP to interchange the elements of list 1 and last positions

k=[]
n=int(input("enter size:"))
for i in range (n):
    i=int(input(i))
    k.append(i)
print(k)
temp=k[0]
k[0]=k[-1]
k[-1]=temp
print(k)
