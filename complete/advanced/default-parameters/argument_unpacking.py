accounts = {
        'checking': 1958.00,
        'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update balance of account->return new balance"""
    accounts[name] += amount
    return accounts[name]

transactions = [
        (-180.67, 'checking'),
        (-220.00, 'checking'),
        (-220.67, 'checking'),
        (-15.70, 'checking'),
        (-23.90, 'checking'),
        (-13.00, 'checking'),
        (-1579.50, 'checking'),
        (-600.50, 'checking'),
        (-600.50, 'checking'),
]

for t in transactions:
    print(add_balance(*t))

# add_balance[t[0], t[1]]
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
        { 'username': 'Klaus', 'password': '123'},
        { 'username': 'Elijah', 'password': '456'}
]
user_objects = [User(username=data['username'], password=data['password']) for data in users]
print(user_objects)
user_objects = [User(**data) for data in users]
print(user_objects)

users = [('Rebekah', '323'), ('Fraeya', '932')]
