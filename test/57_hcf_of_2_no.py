def fn_hcf(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)&(y%i==0)):
            hcf=i
    return hcf
num1=54 
num2=24
print(fn_hcf(num1,num2))

# output 6