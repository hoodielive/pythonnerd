from functools import wraps

def mapper(func):

    @wraps(func)
    def inner(list_of_values):

        """This is the inner()"""
        return [func(value) for value in list_of_values] 
    return inner

@mapper
def camelcase(s):
    """Turn strings_like_this into StringsLikeThis"""
    return ''.join([word.capitalize() for word in s.split('_')]) 

#print(camelcase('some_string'))

names = [
        'rick_ross', 
        'a$ap_rocky',
        'kendrick_lamar',
        'le$_steaknshrimp'
]

print(camelcase(names))
