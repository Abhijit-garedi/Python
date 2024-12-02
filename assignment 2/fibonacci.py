# Module to generate Fibonacci series up to n
def fib(n):
    f1, f2 = 0, 1 
    print(f1, f2, end=" ")

   
    for x in range(2, n):
        f = f1 + f2
        print(f, end=" ")  
        f1, f2 = f2, f  
    print()