#Pyton-3 "for" example

print("\n*** Sort names by length ***\n")

names = [
'Oliver','Jake','Noah','James','Jack','Connor','Liam','John',
'Harry','Callum','Mason','Robert','Jacob','Jacob','Jacob','Michael',
'Charlie','Kyle','William','William','Thomas','Joe','Ethan','David',
'George','Reece','Michael','Richard','Oscar','Rhys','Alexander','Joseph',
 'James','Charlie','James','Charles','William','Damian','Daniel','Thomas'
]

def by_len(el):
	return len(el)

names.sort(key = by_len)

print(names)





