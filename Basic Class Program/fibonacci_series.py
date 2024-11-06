# profram to print fibonacci series  

# SIR METHOD

n = int(input())
a=0
b=1
print(a)
print(b)

for i in range(n-2):
    c = a+b
    print(c)
    a = b
    b = c