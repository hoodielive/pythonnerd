friends = ['Klaus', 'Rebekah', 'Elijah', 'Kol', 'Davina']

start_with_k = filter(lambda friend: friend.startswith('K'), friends)

another_start_with_k = (f for f in friends if f.startswith('K'))

friends_lower = map(lambda x: x.lower(), friends)
