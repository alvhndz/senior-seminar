#lcg.py
import numlib as nl

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
c = R(12121212121) # an element of R
state = 10**10+1

# exercise 1
xgcd(a,m) #to show they're relatively prime
r= m%4  #if this is 0 ...
r_!=(a-1)%4  # ... this must be 0

def prng():
    """Return the next sequential integer between 0 and m-1, inclusive."""
    global state
    state = int(a*state+c) # a*state+c is an element of R = Z/m
    return state
