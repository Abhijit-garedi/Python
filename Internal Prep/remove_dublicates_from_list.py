# remove duplicates from the list 

l = [1,1,2,2,3,3,3]

dl = []

for i in l:
    if i not in dl:
        dl.append(i)
print(dl)


