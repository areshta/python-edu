#Python-3 list example. Lexicographical comparison

print("\n*** List comparing. ***\n")
list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
list3 = [2,3,4,5,0,0]
list4 = [0,0,0,0,0,0,0] 
list5 = [1,1,100,1,1,1,1] 
list6 = [1,2,3,4,5,6,0]
list7 = [[4,2],[3,4]] 
list8 = [[3],[1,0,0]]

print(list2 > list1) # True
print(list3 > list1) # True
print(list4 > list1) # False
print(list5 > list1) # False
print(list6 > list1) # True
print(list8 > list7) # False (recursive comparing) 

list_mix = [["b"], [123]]
#print(list_mix.sort()) #throw exception TypeError: '<' not supported between instances of 'int' and 'str'

print("\n*** List concatenation. ***\n")
list8 = list1 + list5
print(list8) 

print("\n*** List sorting. ***\n")
print(sorted(list8)) # return lis
list5.sort() # do not return list
print(list5)




