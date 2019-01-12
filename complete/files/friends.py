# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`
# hint: readlines() 

friends = input('Enter three friends separated by commas (no spaces please): ').split(',')

people = open('people.txt','r')

people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends) # unordered, remove duplicates

people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}')

nearby_friends_file.close()
