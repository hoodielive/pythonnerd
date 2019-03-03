class Animal:
    type = "mammal"

class Dog(Animal):
    breed = "labrador"

my_dog = Dog()
print(my_dog.breed)
print(my_dog.type)

class Bird(Animal):
    type = "bird"

my_bird = Bird()
print(my_bird.type)

# multiple inheritance
class Eagle(Animal, Bird):
    species = 'eagle'

my_eagle = Eagle()
print(my_eagle.type)