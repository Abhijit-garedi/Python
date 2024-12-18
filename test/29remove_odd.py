#WAPP to remove odd elements from the given list
k = []
n = int(input("enter size:"))
for i in range(n):
    i = int(input("enter number")) 
    k.append(i)
print(k)


for i in k[:]:
    if i % 2 != 0:
        k.remove(i)
print(k)

# output

# enter size:5
# enter number1
# enter number2
# enter number3
# enter number4
# enter number5
# [1, 2, 3, 4, 5]
# [2, 4]