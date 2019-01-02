class Student:
    def __init__(self, name, school):
        self.name = name 
        self.school = school
        self.marks = []

    def average(self): 
        return sum(self.marks) / len(self.marks)
