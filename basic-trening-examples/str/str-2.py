#Python-3 strings example

print("\n*** Slice example. ***\n")

str1 = "123456789"
print('str1 = "123456789"')
print("str1[1] = ", str1[1])
print("str1[2:5] = ", str1[2:5])
print("str1[-2] = ", str1[-2])
print("str1[3:] = ", str1[3:])
print("str1[:3] = ", str1[:3])

print("\n*** Concatination example. ***\n")

str1 = "Johen"
str2 = "Black"
print( str1 + " " + str2 + "\n")

print("\n*** Execution of string as statement example. ***\n")

op ="print('ho-ho')"
exec(op)
