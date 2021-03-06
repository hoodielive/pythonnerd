class Student:
    def __init__(self, name):
        self.name = name

# Python calls the dunder method for your automatically
movies = ['Matrix', 'Finding Nemo']
print(movies.__class__) # list lol
print("hi".__class__)
print(len(movies)) 

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i): # unlocks for loops 
        return self.cars[i] 

    def __repr__(self): # unlock strings
        return f'<Garage {self.cars}>' 

    def __str__(self): # tell me something good
        return f'<Garage with {len(self)} cars.' # call your previous __len__ 

# Objects
ford = Garage() 
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)
print(len(ford.cars))
print(len(ford))
print(ford[0])

# __getitem__ enables looping
for car in ford:
    print(car)
