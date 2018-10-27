#Pyton-3 "for" example

print("\n*** Output names that started from 'J' from the list  ***\n")

names = set([
'Oliver','Jake','Noah','James','Jack','Connor','Liam','John',
'Harry','Callum','Mason','Robert','Jacob','Jacob','Jacob','Michael',
'Charlie','Kyle','William','William','Thomas','Joe','Ethan','David',
'George','Reece','Michael','Richard','Oscar','Rhys','Alexander','Joseph',
 'James','Charlie','James','Charles','William','Damian','Daniel','Thomas'
])


for name in names:
	if name[0] == 'J':
		print(name)




