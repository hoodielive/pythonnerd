class Student:
    def __init__(self, name, school):
        self.name = name 
        self.school = school
        self.marks = []

    def average(self): 
        return sum(self.marks) / len(self.marks)

larry = Student('Larry', 'CMU')
larry.marks.append(95)
larry.marks.append(99)

print(larry.average()) # or print(Student.average(larry))

class Foo:
    @classmethod 
    def hi(cls):
        print(cls.__name__)

my_object = Foo() 
my_object.hi() 

class Bar:
    @staticmethod
    def hi():
        print("Hello, I don't take parameters")

another_object = Bar() 
another_object.hi() 
