#Python-3 access to class variables examples

class A:
    def __init__(self):
        self._a  = 5     # private style
        self.__b = 10    # strong private style
        self.__c = 15
        self.__d = 20

    def set_c(self, c):
        self.__c = c

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d
    
    cc = property(get_c, set_c)
    dd = property(get_d) # dd will be read-only

print("\n*** Class property example ***\n)

a = A()

print(" a._a = ", a._a)         # access is allowed. _ - is style only
print(" a._A__b = ", a._A__b)   # access is allowed by special name. __ - is style only

a.cc = 22
print("a.cc = ", a.cc)
print("a.dd = ", a.dd)
a.dd = 30 # exception: dd is read-only
