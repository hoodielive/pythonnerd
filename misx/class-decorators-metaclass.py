def add_chirp(cls):
    'Class decorator to add speak method'
    def chirp(self):
        return "CHIRP"
    cls.speak = chirp
    return cls

@add_chirp 
class Bird:
    pass 

b = Bird() 
print(b.speak()) 
