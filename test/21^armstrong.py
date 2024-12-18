#Write a python program to print or check it’s a Armstrong number

n=int(input("enter n"))
i=len(str(n))
temp=n
sum=0
while(n>0):
        d=n%10
        sum=sum +d**i
        n=n//10
if(sum==temp):
       print("given number is a Armstrong")
else:
       print("given number is not a Armstrong")


# OUTPUT:

# enter n153
# given number is a Armstrong