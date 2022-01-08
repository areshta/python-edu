# Write a function that returns the odd numbers from a given interval. 
# The default interval is 0-100. The interval is given from standard input

gbegin = 0 #default value
gend = 100 #default value

def odd(begin, end):
    res = []
    for i in range (begin, end + 1, 1):
        if i % 2 != 0:
            res.append(i)
    return res

def input_interval():
    ibegin = gbegin
    iend = gend

    while True:
        s = input ("Enter interval in format <begin> <end>\n example: 3 22\n"+
                    "or pres enter for default interval 0...100 :"
                )
        if s == '':
            break
        else:
            begin, end = s.split(" ")
            ibegin = int(begin)
            iend = int(end)
            if ibegin < iend:
                break
            else:
                print('try again. Bad values :', ibegin, iend)

    return ibegin, iend

begin, end = input_interval()
res = odd(begin, end)
print("Result:", res)

        
    
