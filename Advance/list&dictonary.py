# List comprehension to get even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# Dictionary comprehension to store number and its square
square_dict = {x: x**2 for x in even_numbers}

# Output
print("Even Numbers List:", even_numbers)
print("Dictionary (Number : Square):", square_dict)
