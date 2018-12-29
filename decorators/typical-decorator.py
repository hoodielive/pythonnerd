def camelcase(s):
    """Turn strings_like_this into StringsLikeThis"""
    return ''.join([word.capitalize() for word in s.split('_')]) 

print(camelcase('some_string'))
