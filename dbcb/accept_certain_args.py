def recv(maxsize, *, block):
    'Receives and returns a message'
    return(maxsize, block)

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m 
    print(m)

msg = recv(1024, block=False)
print(recv(1024, block=True))
print(msg)

mininum(1,5,2, -5, 10)
mininum(1,5,2, -5, 10, clip=0)

