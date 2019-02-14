from functools import wraps 

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def spam(a,b,c):
    print(a,b,c)

spam(1,2,3, debug=True)

