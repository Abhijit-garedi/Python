# to print most three common characters from the given strings using counter module

from collections import Counter
s = input("enter strings:")
print(Counter(s).most_common(3))
