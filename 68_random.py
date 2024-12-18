
import random
import string

print("Generate a random alphabet")
print(random.choice(string.ascii_letters))

Max_length=255
str1 = ""

for i in range(random.randint(1, Max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)    


# output
# l
# dhoewohbosdhieghkdngoehgheokhwehogihkgbh