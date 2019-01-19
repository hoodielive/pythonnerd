friends_last_seen = {
    'Keith': 3,
    'Vince': 7, 
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen))
see_friend(friends_last_seen, 'Keith')
print(id(friends_last_seen))

age = 20 

def increase_age(current_age):
    current_age = current_age + 1 
    print(current_age)

print(id(age))
increase_age(age)
print(id(age))
