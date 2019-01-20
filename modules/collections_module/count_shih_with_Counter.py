from collections import Counter

print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(Counter({'a': 2, 'b': 3, 'c': 1}))
print(Counter(a=2, b=3, c=1))

c = Counter()
c.update('abcdefg')
print('Sequence:', c)
