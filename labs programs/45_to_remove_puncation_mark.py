# WAPP to remove puncation symbol in a given string 

p = " & @ * # () {} []"

s = input("enter string")

s1 = ""

for i in s:
    if i not in p:
        s1 += i

print(s1)

