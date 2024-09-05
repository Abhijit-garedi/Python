# a python program to create a list and suffle the list of items using index values

n = int (input("enter size:"));
l = []
for i in range(n):
    i = int(input("enter value:"))
    l.append(i)
    print(l)
    index1 = int(input(i))
    index2 = int(input(j))
    l[index1],l[index2] = l[index2][index1]
    print(l)