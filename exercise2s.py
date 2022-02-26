#exercise2.py
import numlib
from numlib import factor
import math

m = 2**64
a = 214319739410341
c = 12121212121
state = 10**10+1

R = numlib.Zmod(m)  
p = R(0)

#condition for second bullet point: a-1 must be...
# ...divisible by all prime factors of m

factors = list(set(factor(m)))
print('Prime factors of ',m,'are: ',factors)

for fact in factors:
	assert(a - 1) % fact == 0, f'{fact} does not divide a - 1 = {a-1}'

for s in range (40):
	n = (a-1)**s
	if n % m == 0:
		print ('Potency s is: ',s)
		break
