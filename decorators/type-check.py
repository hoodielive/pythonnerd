def require_ints(decorated):
    def inner(*args, **kwargs):
        # Get any values that may have been sent as keyword arguments.
        kwargs_values = [i for i in kwargs.values()]
        
        # Iterate over every value sent to decorated method, and ensure that each one is an integer
        # else raise TypeError
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)

        # Run the decorated method, and return the result. 
        return decorated(*args, **kwarggs)
    return inner
