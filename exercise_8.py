#exercise_8.py
import math

a= 123456789
m=2**64
h = a
h_prime = m
p = 1
p_prime = 0
s = 1 + a**2

q = h_prime / h
u = h_prime - (q*h)
v = p_prime - q*p

if u**2 + v**2 < s:
	h_prime = h
	h = u
	p_prime = p
	p= v
	q = [h_prime / h]
	u = h_prime - (q*h)
	v = p_prime - q*p
	s = u**2 + v**2
else:
	u = u - h
	v = v - p
	s = u**2 + v**2
	v_2 = math.sqrt(s)
	print(v_2)
