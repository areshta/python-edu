import copy
##Python-3 list copy example

print("\n*** list1=list2 is not copy! ***\n")

list1 = []
list2 = [1,2,3,4]
list1 = list2
list2[1] = -1
print(list1) #it is not copy! it is alias

print("\n*** Shallow copy copyes one level only! ***\n")

list1 = []
list2 = [1,[-1,-2,-3],2,3]
list1 = list2.copy()
list2.append(4)
list2[0] = 0;

print("looks as endipendent copy. list1 = ", list1)

list2[1][1] = -10
print("Ops! It was not recursive! References are shared! list1 = ", list1)

print("\n*** Real deep copy ***\n")
list1 = copy.deepcopy(list2)
list2[1][1] = -100
print("Copy.deepcopy is real depp copy ", list1)


