def another_function():
    print('another function')

def turn_into_another_function(func):
    return another_function

@turn_into_another_function
def a_function():
    print('a function')
#a_function = turn_into_another_function(a_function)

a_function() 
