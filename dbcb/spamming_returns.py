def spam(a,b,c,d):
    print(a,b,c,d)
    

from functools import partial 
s1 = partial(spam, 1) # a=1
print(s1)

print(s1(2,3,4)) # 1 2 3 4

print(s1(4,5, 6)) # 1 4 5 6

s2 = partial(spam, d=42)
print(s2)

points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

import math 

def distance(p1, p2):
    x1, y1 = p1 
    x2, y2 = p2 
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)

print(points.sort(key=partial(distance, pt)))
print(points)
