friends = [
    {
        'name': 'Klaus',
        'location': 'New Orleans'
    },
    {
        'name': 'Elijah',
        'location': 'New Orleans'
    },
    {
        'name': 'Marcellus',
        'location': 'New Orleans'
    },
    {
        'name': 'Rebekah',
        'location': 'New Orleans'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby) > 0:
    print('You are not alone!')

print(all([1,2,3,4,5, 0]))
