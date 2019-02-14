# if you only want to evaluate an expression used a lambda function 

add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))

# can be used in context of sortin and data reduction 

names = ['King Steed', 'King Sanchez', 'King Spivey', ]

print(names)
print(sorted(names, key=lambda name: name.split()[-1].lower()))
