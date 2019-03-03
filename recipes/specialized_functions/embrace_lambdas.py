def apply_operator(a, b, f):
    return f(a, b)

print(apply_operator(2, 3, lambda x, y: x * y))
