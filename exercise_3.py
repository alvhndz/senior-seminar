#exercise_3.py
#if gcd(a, m) = d then, modulo m, for any integer x, we have that ax is always a multiple of d

import numlib as nl

m=2**64
a=123456789

R = nl.Zmod(m)
d=nl.gcd(a,m)

print('gcd(a,m) = ',d)
print('Introduce an integer: ')

x = int(input())
k=R(x)
b=a*k

r = b%d

print(' For a =',a, ', m =',m,'d = ',d, 'a*x(mod(m)) % d =', r)

