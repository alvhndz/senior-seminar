#fermat.py

import numlib

n=0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd
def sqroot(n):
    """return sqrt(n) if integer n is a perfect square; otherwise, return 0"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return lower if lower ** 2 == n else upper if upper ** 2 == n else 0
    
def ceil_sqroot(n):
    """return integer ceiling(sqrt(n)) where n is a positive integer"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return upper
    
def fermatfactor(n):
    a = ceil_sqroot(n)
    b = sqroot(a*a - n)
    while not b:
        a += 1
        b = sqroot(a*a - n)
    return int(a - b)
    
print(fermatfactor(n))
print(a)
print(b)
