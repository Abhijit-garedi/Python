# python program to print a almmutative sum of the list of element
def cumulative_sum(lst):
    cum_sum = [] 
    total = 0 
    for num in lst:
        total += num 
        cum_sum.append(total)  
    return cum_sum  
# Example usage
n = int(input("Enter number of elements: "))  # Get the number of elements
elements = []

for i in range(n):  
    elements.append(int(input(f"Enter element {i + 1}: ")))

result = cumulative_sum(elements)  
print("Cumulative sum list:", result)  
