#to convert list into nested dictornary keys
l=[]
n=int(input("enter size:"))
for i in range(n):
    i=int(input("enter value:"))
    l.append(i)

print(l)
d=c={}
for i in l:
    c[i]={}
    c=c[i]
    print(d)    