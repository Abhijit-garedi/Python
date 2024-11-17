# Pr30:-
# WAPP to print cumulative sum of list of elements
k=[]
n=int(input("enter size:"))
for i in range(n) :
    i=int(input(i))
    k.append(i)
print(k)
sum=0
c=[]
for j in k:
    sum+=j
    c.append(sum)
print(c)
