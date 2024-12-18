import string
def is_pangram(input_string):

    Alphabet_set=set(string.ascii_lowercase)
    input_set=set(input_string.lower())
    return Alphabet_set.issubset(input_set)

input_string=input("enter string")
if is_pangram(input_string):
      print("pngram")
else:
      print("not a pangram")


#output
# enter stringthe quick brown fox jumps over the lazy dog
# pngram