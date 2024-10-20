#to print characters from the given list which are occuring more than n times & less than n times

from collections import Counter
from itertools import chain

def max_aggregate(list_str,N):

    temp=(set(sub)for sub in list_str)
    counts=Counter(chain.from_iterable(temp))

    gt_N=[chr for chr, count in counts.items() if count > N]
    lt_N=[chr for chr, count in counts.items() if count < N]

    return gt_N,lt_N

list_str=['abed','iabhf', 'dslsdf', 'sdfsas','jlkdfgd']
print("original list:")
print(list_str)

N=3
result = max_aggregate(list_str, N)

print("\ncharacters of the said list of strings in whcih occurs less than:",N)
print(result[1])


