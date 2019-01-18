# a generators is a function that remembers the state its in between executions (the last thing its done)

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1

g = hundred_numbers()
#print([x * 2 for x in hundred_numbers()])

print(next(g))

