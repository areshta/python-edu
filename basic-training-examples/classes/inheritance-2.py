#Python-3 inheritance example

#Base class 
class Base:
    c = 8
    def __init__(self):
        self.a = 5
        self.b = 7

    def out(self):
        print ("Base")

    def val(self):
        print("a = ", self.a, ";   b = ", self.b,  ";   c = ", Base.c) 

class Child(Base):
    def __init__(self):
        super().__init__()
        self.a = 555

    def out(self):
        print("Chaild of ")
        super().out()

    def val(self):
        print("a = ", self.a, ";   b = ", self.b,  ";   c = ", Base.c) 

print("=== class Base ===")
b = Base()
b.out()
b.val()

print("=== class Child ===")
c = Child()
Base.c = 999
c.out()
c.val()
