n = int(input("Enter a number: "))  # Number of elements
l = []

# Input elements into the list
for i in range(n):
    value = int(input("Enter value: "))
    l.append(value)

# Remove odd numbers from the list
l = [i for i in l if i % 2 == 0]

print(l)  # Output the list after removing odd numbers
