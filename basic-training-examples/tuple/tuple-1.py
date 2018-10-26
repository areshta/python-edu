#Python-3 tuple examples

print("\n*** Simple tuple ***\n")
seasons = ("winter", "spring", "summer", "autumn")
print("There are enough tuples in real life.\nSeasons, for example: ", seasons)

print("\n*** Create tuple from list ***\n")
a, b = 3, 4
c = tuple([a,b])
print(c)

print("\n*** Function can return tuple ***\n")
def zero_coord():
	return 0,0 
zc = zero_coord()
print(zc)

print("\n*** Tuple as a key of a dictionary ***\n")
half_life = {	("uranium",235):7.04e8,
				("uranium",238):4.468e9,
				("plutonium",239):2.41e4,
				("plutonium",240):6500
			}
print("Half-life of uranium-238 = ", half_life[("uranium",238)] )

print("\n*** Tuple can include references to changing values ***\n")
tp = ([10],) # if you miss ',' it will be integer in parentheses
print("Tuple includes list. tp[0][0] = ", tp[0][0])
tp[0][0] = -100
print("The list inside tuple was changed. tp[0][0] = ", tp[0][0])
	
