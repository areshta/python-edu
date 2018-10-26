# python-3 List + for example
print ("\n*** Matrix example ***\n")

matrix = [[11,12,13],[21,22,23],[31,32,33]]

for line in matrix:
    for elem in line:
        print (str(elem)+" ",end = '')
    print("")

print("Central element:", matrix[1][1]);
