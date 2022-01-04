def MyRange(start,stop,step=1):
    current = start
    while current < stop:
        yield current
        current += step

x = MyRange(1,10,2)
for i in x:
    print(i,end = ' ')
    
y = MyRange(0,3)
it = y.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())