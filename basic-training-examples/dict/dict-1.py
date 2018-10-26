# Python-3 dictionary example
# For example, we registrate some colored objects
# and whant to know how many objects of every color was.

# was registrated:
colors = ["red","blue","red", "cyan", "black", "blue", "red", 
          "red", "orange", "black", "cyan", "red", "pink",
          "orange", "black", "cyan", "red", "pink", "blue",
          "red", "green", "blue", "red", "green", "blue", 
          "blue","red", "cyan", "black", "blue", "green"]

dc = {} # we will use dictionary of color:counter pairs
for cl in colors:
    if dc.get(cl) == None:
        dc[cl] = 1
    else:
        dc[cl] = dc[cl]+1

print(dc) 
