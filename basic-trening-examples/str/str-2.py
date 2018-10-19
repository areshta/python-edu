#Python-3 strings example

print("\n*** Slice example. ***\n")

str1 = "123456789"
print('str1 = "123456789"')
print("str1[1] = ", str1[1])
print("Pay attention. The last number in the slice is point after diapason!")
print("Substring str1[2:5] includes charecters #2,#3,#4 (not #5!)")
print("str1[2:5] = ", str1[2:5])
print("str1[-2] = ", str1[-2])
print("str1[3:] = ", str1[3:])
print("str1[:3] = ", str1[:3])
print("str1[:] = ", str1[:])

print("\n*** Concatination example. ***\n")

str1 = "Johen"
str2 = "Black"
print( str1 + " " + str2 + "\n")

print("\n*** Convertion example. ***\n")
str_to_int = int("125")
print("str_to_int = ", str_to_int)
float_to_str = str("27.5")
print("float_to_str = " + float_to_str)


print("\n*** Execution of string as statement example. ***\n")

op ="print('ho-ho')"
exec(op)
