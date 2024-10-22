#wrie a python program to remove puncation form the string

s=" & @ * # () {} []"

s1 = input("enter string:")

s2=""

for i in s1:
    if i not in s:
        s2=s2+i

print(s2)