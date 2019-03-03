def generate_scaler(a):
    return lambda x: a * x

doubler = generate_scaler(2)
print(doubler)
tripler  = generate_scaler(3)
print(tripler)