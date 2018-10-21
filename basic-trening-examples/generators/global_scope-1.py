#Python-3. Example of using r/w global scope variables.
# 10 points of Fibonacci sequence

current = 1
next = 1
def fibonacci():
    global current
    global next
    prev =  current
    current = next
    next = prev + current
    return prev

for i in range(10):
    print(fibonacci())
