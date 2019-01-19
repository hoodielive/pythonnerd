friends = ['Klaus', 'Rebekah', 'Elijah', 'Kol', 'Davina']

start_with_k = filter(lambda friend: friend.startswith('K'), friends)

another_start_with_k = (f for f in friends if f.startswith('K'))

friends_lower = map(lambda x: x.lower(), friends)

class User:
    def __init__(self, username, password):
        self.username = username 
        self.password = password

    @classmethod 
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

user = [
        { 'username': 'Klaus', 'password': '123' }
        { 'username': 'Elijah', 'password': '456' }
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)
