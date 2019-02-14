x = 10
print(x)
a = lambda y: x + y 
print(a(10))
x = 20 
print(x)
b = lambda y: x + y 
print(b(10))
print(a(10))

funcs = [lambda x: x+n for n in range(5)]

for f in funcs: 
    print(f(0))


funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))

funcs = [lambda x, n=n: x+n for n in range(5)]
f = [f for f in funcs]
print(f[0])
