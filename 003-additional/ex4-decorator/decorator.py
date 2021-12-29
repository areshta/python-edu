x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

class Functor:
    def __init__(self, divider):
        self.divider = divider
    def __call__(self, dividend):
        return dividend % self.divider == 0

def Attention(lv):
    def decorator(fn):        
        def wrapped(predicate,*args, level = lv): 
            return "<h1>"+str(fn(predicate,*args, level = lv))+"</h1>"
        return wrapped
    return decorator

@Attention(75)
def sumP(predicate,*args, level = 0):
    sum = 0
    for arg in args:
        if predicate(arg):
            sum+=arg
            if sum > level:
                break
    return sum

p1 = Functor(2)
p2 = Functor(3)

print(sumP(p1,*x))
print(sumP(p2,*x))
