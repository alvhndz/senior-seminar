m = 2**64
a = 123456789
c = 12121212121
state = 10**10+1

def prng():
    """Return the next sequential integer between 0 and m-1, inclusive."""
    global state
    state = (a * state + c) % m
    return state
