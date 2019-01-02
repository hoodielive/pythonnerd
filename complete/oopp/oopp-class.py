my_student = {
        'name': 'Cool Dude', 
        'grades': [70, 88, 90, 99], 
        'average': None # something here - maybe a Symbol
}

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades 

    def average(self):
        return sum(self.grades) / len(self.grades) 

student_one = Student('hood', [70, 88, 90, 99])

print(student_one.__class__)
print(student_one.name)

student_two = Student('Jose', [99, 98, 97, 96])
print(student_two.name)

print(student_one.average()) # self is the object that calls this function 
print(Student.average(student_one)) # or you can call it like this - but why would you?  


