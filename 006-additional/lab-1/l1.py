#Write a function that returns the sum of n numbers
def sum(*args):
    s = 0
    for x in args:
        s += x
    return s

print(sum(5,5,5,2,3))
