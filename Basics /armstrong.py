n = int(input())
sum = 0
order = len(str(n))
temp = n

while temp > 0:
    r = temp % 10
    sum += r ** order
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("No Armstrong")
