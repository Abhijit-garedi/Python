# write a python program to interchange the element of list first & last position 

# Input: Number of elements in the list
n = int(input("Enter size of list: "))  
l = []

# Populating the list with values
for i in range(n):
    value = int(input("Enter value: "))
    l.append(value)

print("Original List:", l)

# Interchanging the first and last element if the list has more than 1 element
if len(l) > 1:  
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp

print("List after interchanging first and last elements:", l)
