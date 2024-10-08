# program to print or count the alphabets present in a string 

def char_count(input_string):
    count={}
    for c in input_string:
        if c in count:
            count[c]+=1
        else:
                count[c]=1
    for char,cnt in count.items():
        print(f"'{char}':{cnt}'")
input_string=input("enter string:")
char_count(input_string)
