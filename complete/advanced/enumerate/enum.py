top_friends = ['Klaus', 'Marcell', 'Elijah']

for i, friend in enumerate(top_friends):
    print(f'Top villians are {i+1} friend is {friend}')


friend_g = enumerate(top_friends)
k, v = next(friend_g)
print(next(friend_g))
print(k)
print(v)




