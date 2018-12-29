# a decorator is just a function that expects another function, and does something with it

def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func

def add(x, y):
    """Return the sum of x and y."""
    return x + y 
add = decorated_by(add)
