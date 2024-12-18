#WAPP to find sum of n natural numbers using recursive function
def fn_recur(n):
    if n<=0 :
        return 0
    else :
        return n+(fn_recur(n-1))
num=5
print(fn_recur(num))

# output:
#  15