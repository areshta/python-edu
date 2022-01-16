#Write a python function to print a dictionary where the keys are numbers
#between 1 and n (both included) and the values are square of keys. “n” is
#passed as function parameter.

import math

def fn(n):
    res = dict()
    for i in range(1,n+1):
        res[i] = i*i
    return res

print( fn(5) )
