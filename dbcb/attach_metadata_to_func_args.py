# You've written a function, but would like to attach some additional information to the args so that others
# Know more about how a function is supposed to be used. 

def add(x:int, y:int) -> int: 
    return print(x + y)

add(5, 6)
print(add.__annotations__)
