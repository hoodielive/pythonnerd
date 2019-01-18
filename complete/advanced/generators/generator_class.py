class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1 
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

print(sum(FirstHundredGenerator()))
    
for i in FirstHundredGenerator():
    print(i)

class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)

#class FirstHundredIterable:
#    def __iter__(self):
#        return FirstHundredGenerator()

#class FirstHundredIterator:
#    def __init__(self):
#        self.numberes = [1,2,3,4,5]
#        self.i = 0
#
#    def __next__(self):
#        if i < len(self.numbers):
#            current = self.numbers[self.i]
#            i += 1 
#            return current
#        else:
#            raise StopIteration()

my_gen = FirstHundredGenerator()
print(my_gen.number)
my_gen.__next__()
print(next(my_gen))
print(my_gen.number)


