# wapp a program to replace string characters in all occurence accept its first occurance 



s = "aitam"

ch = s[0]

s1 = s.replace(ch, "@")

s1 = ch +s1[1:]

print(s1)