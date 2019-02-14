def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


def spammer(a, b=None):
    if b is None:
        b = []
        b.append(a)
    print(b)

spammer('Forty')


_no_value = object() 
def spamming(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied :)')


spamming('I know a change will come - Sam Cooke')
