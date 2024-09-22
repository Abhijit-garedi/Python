# progera using function with return keyword 
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fact(n-1) * n

b = 5
print(fact(b))
