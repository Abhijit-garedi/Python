#Write a python program to print largest element in the list

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


# OUTPUT
# enter size:4
# 0 4
# 1 5
# 2 9
# 3 7
# ['4', '5', '9', '7']
# 9