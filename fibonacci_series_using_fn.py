# program using function 

import math

def is_fibonacci(n):
    return (math.isqrt(5 * n * n + 4) ** 2 == 5 * n * n + 4) or \
           (math.isqrt(5 * n * n - 4) ** 2 == 5 * n * n - 4)

num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
