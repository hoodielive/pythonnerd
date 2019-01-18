#def starts_with_k(friend):
#    return friend.startswith('K')

friends = ['Klaus', 'Marcel', 'Mikel', 'Elijah', 'Rebekah', 'Fynn', 'Fraeyah', 'Esther', 'Kol'] 

#start_with_k = filter(start_with_k, friends)
#print(next(start_with_k))

start_with_k = filter(lambda x: x.startswith('K'), friends)
print(next(start_with_k))
# or 
start_with_k = filter(lambda friend: friend.startswith('K'), friends)
print(next(start_with_k))
another_starts_with_k = (f for f in friends if f.startswith('K'))
print(next(another_starts_with_k))

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

print(next(start_with_k))
print(next(start_with_k))
print(next(start_with_k))
