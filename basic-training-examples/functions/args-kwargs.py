#Python-3. function with variadic number of arguments

print("\n*** Example of using of function with variadic number of arguments***\n")

def sum(*args):
    s = 0
    for ar in args:
        s += ar
    return s

def fun(*args, **kwargs):
    for ar in args:
        print (ar)
    for key in kwargs:
        print (key,":",kwargs[key])

fun(1,2,"abc",[5,6], name = "Ann", age = 10)

s = sum(1,2,3,4,5)
print("summa 1..5 = ", s)
