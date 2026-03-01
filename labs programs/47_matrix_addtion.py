#write a python program to preform matrix addtion

a=[[1,2,3],[4,5,6],[8,8,9]]

b=[[0,2,7],[6,5,11],[3,6,1]]

c= [[0,0,0],[0,0,0],[0,0,0]]

print("a=",a)

print("b =",b)

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]

for i in range(len(c)):
    print("c =", c[i])

