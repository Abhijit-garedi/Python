# a python program to create a list and suffle the list of items using index values

n = int(input("Enter size: "))
l = []

# Input list values
for i in range(n):
    value = int(input("Enter value: "))
    l.append(value)

print("Original list:", l)

# Input indexes to shuffle
index1 = int(input("Enter the first index to swap: "))
index2 = int(input("Enter the second index to swap: "))

# Swap the elements at index1 and index2
l[index1], l[index2] = l[index2], l[index1]

print("List after swapping:", l)
