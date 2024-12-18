l=[]
n=int(input("enter size:"))
for i in range(n):
    i=int(input(i))
    l.append(i)
print(l)
d=c={}
for i in l:
    c[i]={}
    c=c[i]
print(d)


# output:
# enter size:4
# 0 1
# 1 2
# 2 3
# 3 4
# [1, 2, 3, 4]
# {1: {2: {3: {4: {}}}}}