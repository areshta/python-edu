# Write a generator that implements the Fibonacci algorithm

def fibonachi():
    a = 1
    b = 1
    while True:
        yield a
        b , a = a , a + b

i = 0
for f in fibonachi():
    print(f)
    if i  == 10:
        break;
    i += 1
