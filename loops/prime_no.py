# program to print prime numbers betn the two numbers

   
a = int(input("first num: "))
b = int(input("second num: "))

for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
             if(i % j == 0):
                break

    else:
                print(i)

