# a decorator is just a function that expects another function, and does something with it

def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func

def add(x, y):
    """Return the sum of x and y."""
    return x + y 
add = decorated_by(add)

def also_decorated_by(func): 
    pass

# the above can be done better 
@also_decorated_by
@decorator_by
def add(x, y):
    """Return the sum of x and y."""
    return x + y 

# the above is syntactically equivalent to: add = also_decorated_by(decorated_by(add))
# the function call will be from botton to top
# the add function will execute normally, then the decorated_by being sent to the decorated method 
# decorated_by will return its own callable (in this case a modified add)
# the returned value from decorated_by will be sent to also_decorated_by

