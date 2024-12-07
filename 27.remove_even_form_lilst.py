#write a python program to remove even number from the list

n = int(input("enter number: "))
l = []

for i in range(n):  # Populate the list with user inputs
    l.append(int(input(f"Enter element {i + 1}: ")))

for i in l[:]:  # Iterate over a copy of the list
    if i % 2 == 0:
        l.remove(i)

print(l)

print(LookupError)
