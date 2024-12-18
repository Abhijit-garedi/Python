k = []
n = int(input("enter size:"))
for i in range(n):
    i = int(input("Enter number: ")) 
    k.append(i)
print(k)
for i in k[:]: 
    if i % 2 == 0:
        k.remove(i)
print(k)


# output:
# enter size:3
# Enter number: 1
# Enter number: 2
# Enter number: 3
# [1, 2, 3]
# [1, 3]