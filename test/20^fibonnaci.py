# Write a python program to print fibonnaci series
n=int(input("enter n"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):

    c=a+b
    print(c)
    a=b
    b=c

#output:
# 0
# 1
# 1
# 2
# 3
