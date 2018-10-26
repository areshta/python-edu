#Python-3 list example

print("\n*** List comparing. ***\n")

list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
list3 = [2,3,4,5,0,0]
list4 = [0,0,0,0,0,0,0] 
list5 = [1,1,100,1,1,1,1] 
list6 = [1,2,3,4,5,6,0]

print(list2 > list1) # True
print(list3 > list1) # True
print(list4 > list1) # False
print(list5 > list1) # False
print(list6 > list1) # True

print("\n*** List concatination. ***\n")

list8 = list1 + list5
print(list8) 

print("\n*** List sorting. ***\n")

print(sorted(list8)) # return lis

list5.sort() # do not return list
print(list5)




