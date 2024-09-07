# write a python program to interchange the element of list first & last position 

n = int(input())  
for i in range(n):
    l.append(i)  
print(l) 

if len(l) > 1:  
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp

print(l) 