class Registry(object):
    def __init__(self):
        self._functions = []

    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    def run_all(self, *args, **kwargs):
        return_values = []
        for func in self._functions:
            return_values.append(func(*args, **kwargs))
        return return_values

# um.. 
a = Registry()
b = Registry() 

@a.register
def examp3(x=3):
    return x

@b.register
def examp4(x=5):
    return x

@a.register
@b.register
def examp5(x=7): 
    return x

a.run_all() 
b.run_all()
