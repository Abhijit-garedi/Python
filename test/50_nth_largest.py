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


# output
# enter size3
# enter value1
# enter value2
# enter value3
# [0, 1, 2]
# [2, 1, 0]
# enter n largest1
# 1 is in place 2