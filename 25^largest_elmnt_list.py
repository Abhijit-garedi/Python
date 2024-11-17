k=[]
n=int(input("enter size:"))
for i in range (n):
    i=input(i)
    k.append(i)
print(k)
max=k[0]
for i in range (n):
    if(k[i]>max):
        max=k[i]
print(max)   
