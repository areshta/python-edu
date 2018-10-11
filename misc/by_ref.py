def fun1():
	i = 1
	fun2(i)
	print ("i=", i)

def fun2(i):
	ii = i
	ii += 1
	print ("ii=", ii)

fun1()
