#Python-3. Functions example. Recursion and itteration. 
#          Can be used as module. 
#          Help can be call in Python interactive mode

def factorial_rc(n):
    """recursive solution"""
    if n<1:
        return 1
    else:
        return n * factorial_rc(n-1)

def factorial_it(n):
    """itterative solution"""
    mp = 1
    for i in range(2, n+1):
        mp *= i
    return mp

if __name__ == "__main__":

    print("\n*** Factorial calculation. Recursive and Itteration ***\n")

    for i in range(1,11):
        print("{:2}! = recursive {:8}   and   itterative {:8}"
                .format(i, factorial_rc(i), factorial_it(i)) )

    print("\nUsing docstring inside programm:")
    print(factorial_rc.__doc__)
    print(factorial_it.__doc__)
