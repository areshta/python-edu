#Python-3 inheritance example

#Base class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Child class 1
class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    def __str__(self):
        return f"{type(self).__name__}\n\tname: {self.name}, age: {self.age}, group: {self.group}"

#Child class 2
class Lecturer(Person):
    def __init__(self, name, age, chair):
        super().__init__(name, age)
        self.chair = chair

    def __str__(self):
        return f"{type(self).__name__}\n\tname: {self.name}, age: {self.age}, chair: {self.chair}"

#Start of execution
print("Some University staff:")
lecturer = Lecturer("Johen", 53, "Programming and mathematics")
students = [Student("Alex", 18, "PM-183"),Student("William", 19, "PM-183"), Student("Georg", 18, "PM-183")]
print(str(lecturer))
for student in students:
    print(str(student))

