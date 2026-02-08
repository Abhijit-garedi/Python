# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda 1 even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Lambda 2 square the even numbers
squared_numbers = list(map(lambda x: x ** 2, even_numbers))

# Lambda 3 add 10 to each squared number
final_result = list(map(lambda x: x + 10, squared_numbers))

# Output
print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Squared Even Numbers:", squared_numbers)
print("Final Result:", final_result)
