from collections import Counter, defaultdict, OrderedDict, namedtuple

"""
counter 
defaultdict
OrderedDict
namedtuple
deque
"""

# counter
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

print(Counter({'hello': 5, 'hi': 3})['hi'])

# defaultdict
coworkers = [('Joel', 'MIT'), ('Larry', 'MIT'), ('Vince', 'Harvard'), ('Keith', 'Oxford')]

alma_maters = {}

for coworker in coworkers:
    if coworker[0] not in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])

# destructured 
for coworker, place in coworkers:
    if coworker not in alma_maters:
        alma_maters[coworker] = []
    alma_maters[coworker].append(place)

# or just do 
alma_maters = defaultdict(list) 

print(alma_maters['Joel'])
print(alma_maters['Hood'])


our_company = ['Joel', 'Larry', 'Atum']
other_companies = [('Dude', 'Apple'), ('Anna', 'Lambda hoes')]

co = defaultdict(lambda: our_company)

for person, company in other_companies:
    co[person] = company

print(co[our_company[0]])


o = OrderedDict()
o['Joel'] = 6
o['Keith'] = 12
o['Atum'] = 3

print(o)

o.move_to_end('Keith', last=False)

# namedtuple
Account = namedtuple('Account', ['name', 'balance']) 

account = Account('checking', 1850.90)
print(account.name)
print(account)
