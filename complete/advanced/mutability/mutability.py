friends_last_seen = {
    'Keith': 37,
    'Vince': 34, 
}

print(id(friends_last_seen))

# mutable 

friends_last_seen['Keith'] = '1'
print(id(friends_last_seen))
