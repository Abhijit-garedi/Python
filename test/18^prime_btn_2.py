#Write a python program to print prime numbers between two numbers
a=int(input("enter a:"))
b=int(input("enter b:"))
for i in range(a,b+1):
   for j in range(2,i):
        if(i%j==0):
            break
   else:
        print(i)



# output

# enter a:5
# enter b:15
# 5
# 7
# 11
# 13