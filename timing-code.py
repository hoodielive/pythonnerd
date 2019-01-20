import time

def powers(limit):
    return [x**2 for x in range(limit)]

start = time.time()
powers(500000000)
end = time.time()
print(end - start)

