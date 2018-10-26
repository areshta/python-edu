#Python-3 list copy exampleimport copy
print("\n*** list1=list2 is not copy! ***\n")

list1 = []
list2 = [1,2,3,4]
list1 = list2
list2[1] = -1
print("list1 = list2 is not copy!\nlist2 = ", list2)
print("list1 = ", list1)

print("\n*** Shallow copy copies one level only! ***\n")

list1 = []
list2 = [1,[-1,-2,-3],2,3]
list1 = list2.copy()
list2.append(4)
list2[0] = 0;

print("looks as independent copy. \nlist2 = ", list2)
print("list1 = ", list1)

list2[1][1] = -10
print("\nOps! It was not recursive! References are shared!\nlist2 = ", list2)
print("list1 = ", list1)

print("\n*** Real deep copy ***\n")
list1 = copy.deepcopy(list2)
list2[1][1] = -100
list2[0]=-10
list2.append(-200)
print("copy.deepcopy is real deep copy.\nlist2 = ", list2)
print("list1 = ", list1)



