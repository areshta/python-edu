# Python-3. Using generators
# 10 points of Fibonacci sequence

def fibonacci():
    current = 0
    next = 1
    while True:
        prev =  current
        current = next
        next = prev + current
        yield prev

sq = fibonacci() 

for i in range(10):
    print (next(sq))

