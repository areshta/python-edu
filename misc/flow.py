a = 100
if a > 10:
	print ("a>10")
elif a > 3:
	print ("a>3")
elif a > 4:
	print ("a>4") #the first branch only!
else:
	print ("else")


for i in range(10):
	if i==a:
		break;
else:
	print ("for was not broken!")
print ("after for!")
	
