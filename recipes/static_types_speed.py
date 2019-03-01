def f(x):
    return x**2-42

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for I in range(N):
        s += f(a+i*dx)
    return s*dx

import cython

def f(double x):
    return x**2-42

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for I in range(N):
        s += f(a+i*dx)
    return s*dx
