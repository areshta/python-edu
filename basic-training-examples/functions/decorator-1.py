#Python3 decorator example
#@deco_demor is the same hello = deco_demo(hallo). 

def deco_demo(fun):
    def wrapper():
        print("Pre-call actions")
        ret = fun()
        print("After-call actions")
        return ret
    return wrapper

@deco_demo
def hello():
    print("Hello!")
    return True

print(hello())

