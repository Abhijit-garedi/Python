#WAPP to print pascal triangle using functions
def pascal_triangle(n):
    tr=[1]
    y=[0]
    for i in range(n):
        print(tr)
        tr=[l+r for l,r in zip(tr+y,y+tr)]
pascal_triangle(5)


# output
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]