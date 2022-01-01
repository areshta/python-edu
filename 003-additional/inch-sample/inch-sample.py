# The key to subclassing immutable types is to use __new__ for both object creation and initialisation.
# Float is immutable type

class Inch(float):    
    def __new__(cls,arg = 0.0):
        return float.__new__(cls,arg/2.54)


x = Inch(12)
print(x)
