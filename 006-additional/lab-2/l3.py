# Write a python program to flatten a nested list

#1
import itertools
import copy

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print("Example 1. source:", my_list)

flat_list = list(itertools.chain(*my_list))
print("Example 1. result:", flat_list)

def clean_list(l) -> list:
    for i in range(0,len(l)):
        if type(l[i]) is type([]):
            if len(l[i]) > 0:
                tmp = copy.deepcopy(l[i])
                del l[i]
                for el in tmp:
                    l.insert(i,el)
                    i += 1
                clean_list(l)
                break
            else:
                l[i] = None            
    return l

my_list = [[[[[1]]]], [[2, 3]], [4, 5, 6, 7], [[]], 8, 9]
print("Example 2. source: ", my_list)

flat_list = clean_list(my_list)
print("Example 2. result: ", flat_list)
