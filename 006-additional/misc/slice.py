l1 = ['abcd', 786, 2.23, 'john', 70.2]
print("l1:",l1)
print ("l1[0]: ",l1[0]) # Prints first element of the list -> abcd
print ("l1[-1]: ",l1[-1]) # Prints last element of the list -> 70.2
print ("l1[1:3]: ",l1[1:3]) # Prints elements starting from 2nd till 3rd -> [786, 2.23]
print ("l1[2:]: ",l1[2:]) # Prints elements starting from 3rd element -> [2.23, 'john', 70.2]
print ("l1[::-1]: ",l1[::-1]) # Reverses the list
#Example of slice assignment:
l1[0:2] = [1, 2] # Replace some items
print(l1) # Prints [1, 2, 2.23, 'john', 70.2]
l1[0:2] = [] # Remove some items
print(l1) # Prints [2.23, 'john', 70.2]
l1[1:1] = ['insert1', 'insert2'] # Insert some items
print(l1) # Prints [2.23, 'insert1', 'insert2', 'john', 70.2]
l1[:0] = l1 # Insert a copy of itself at the beginning
print(l1) # Prints [2.23, 'insert1', 'insert2', 'john', 70.2, 2.23, 'insert1', 'insert2', 'john', 70.2]
l1[:] = [] # Clear the list
print(l1) # Prints []

l2 = [1,2,3,4,5,6]
print(l2)
print("l2[0:6:1] :", l2[0:6:1])