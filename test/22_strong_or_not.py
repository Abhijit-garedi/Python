n=int(input("enter n"))
fact=1
temp=n
sum = 0
while(n>0):


    d=n%10
    fact=1
    for i in range(1,d+1):

        fact=fact*i
    sum = sum + fact
    n=n//10
if(sum==temp):
      print("given number is a strong number")
else:
      print("given number is not a strong number")
 
 
 #output 
 #enter n145
#given number is a strong number