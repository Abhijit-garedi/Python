# python program to print a almmutative sum of the list of element

# Function to calculate cumulative sum
def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num  # Add current number to the total
        cum_sum.append(total)  # Append the total to the cumulative sum list
    return cum_sum

# Example usage
n = int(input("Enter number of elements: "))  # Get the number of elements
elements = []

for i in range(n):  # Populate the list with user inputs
    elements.append(int(input(f"Enter element {i + 1}: ")))

print("Cumulative Sum:", cumulative_sum(elements))  # Print the cumulative sum
