from collections import defaultdict, namedtuple, Counter, deque
import csv
import random 
from urllib.request import urlretrieve

# namedtuple
user = ('larry', 'coder')
print(f'{user[0]} is a {user[1]}') 
User = namedtuple('User', 'name role')
user = User(name='larry', role='coder')
print(user.name)
print(user.role)
print(f'{user.name} is a {user.role}')

# defaultdict 

