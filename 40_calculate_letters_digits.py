
# wapp in which accept string or statements calculate the number of letters and digits


data = input('input a string')

d = k = 0

for i in data:
    if i.isdigit():
        d = d + 1

    elif i.isalpha():
        k = k + 1

    else:
        pass    

print("the total letters is :", k)

print('the total alpha is', d)