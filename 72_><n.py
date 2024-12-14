from collections import Counter
from itertools import chain
def max_aggregate(list_str,N):
         temp=(set(sub) for sub in list_str)
         counts= Counter(chain.from_iterable(temp))
         gt_N=[chr for chr,count in counts.items() if count >N]
         lt_N=[chr for chr,count in counts.items() if count <N]
         return gt_N,lt_N
list_str = ['abcd','gibhs','sgsgf','rywe','qweiop']
print("original list:")
print(list_str)
N=3
result= max_aggregate(list_str,N)
print("\n characters of the said list more than :",N)
print(result[0])
print("\n characters of the said list less than :",N)
print(result[1])
 
 