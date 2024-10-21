# program to print a pascal triangle

def pascal_triangle(n):
    tr = [1]
    y = [0]
    for i in range(n):
        print (tr)
        tr = [l+r for l, r in zip(tr+y, y+tr)]
pascal_triangle(5)        