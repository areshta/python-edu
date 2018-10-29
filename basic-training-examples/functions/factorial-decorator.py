#Python-3. Functions example. Recursion and itteration. Decoration.

def counter(func):
    """ counter decorator"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
def factorial_rc(n):
    """recursive solution"""
    if n<1:
        return 1
    else:
        return n * factorial_rc(n-1)

@counter
def factorial_it(n):
    """itterative solution"""
    mp = 1
    for i in range(2, n+1):
        mp *= i
    return mp

print("\n*** Factorial calculation. Recursive and Itteration. Decorators using ***\n")
i = 20
print("{:2}! = recursive {:8}   and   itterative {:8}"
      .format(i, factorial_rc(i), factorial_it(i)) )

