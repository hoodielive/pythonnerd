
# multiple inheritance
class Eagle(Animal, Bird):
    species = 'eagle'

my_eagle = Eagle()
print(my_eagle.type)