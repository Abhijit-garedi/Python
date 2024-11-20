#Pr63:-
#WAPP to print the character count using python modules
 
from collections import Counter
text = input("Enter a string: ")
char_count = Counter(text)
for char, count in char_count.items():
    print(f"'{char}': {count}")
