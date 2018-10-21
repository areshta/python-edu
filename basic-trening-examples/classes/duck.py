# Python-3. Duck conseption
# If it looks like a duck, swims like a duck, 
# and quacks like a duck, then it probably is a duck

# Classes declaration
class Dog:
    def voice(self):
        print("Bark-bark")

class Cat:
    def voice(self):
        print("Meow-meou")

class Duck:
    def voice(self):
        print("Quack-quak")

# Execution 
animals = []
animals.append(Dog())
animals.append(Cat())
animals.append(Duck())

# Python does not need interface inharitance
# It is enough to have the same functions interface

for animal in animals:
    animal.voice()

