class Student: 
    def __init__(self, name, school):
        self.name = name 
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5

larry = WorkingStudent('Larry', 'CMU', 95.50)
print(larry.salary)
print(larry.school)

revjoel = WorkingStudent('Joel', 'MIT', 120.0) 
print(revjoel.salary)
