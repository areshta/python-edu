#Python-3 Lambda example

print("\n Sorting list by abs values using lambda ")

ls = [0,-1,5,-10,20,-2,-7]

ls.sort(key=lambda x: abs(x) )

print(ls)
