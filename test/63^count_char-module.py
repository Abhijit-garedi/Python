#WAPP to print the character count using python modules

from collections import Counter

text = input("Enter a string: ")
char_count = Counter(text)

for char, count in char_count.items():
    print(f"'{char}': {count}")


# output:
# enter string: Nepal
# 'N': 1
# 'e': 1
# 'p': 1
# 'a': 1
# 'l': 1