#exercise_8.py

h = a;
h_prime = m;
p = 1;
p_prime = 0;
s = 1 + a**2;

q = [h_prime / h];
u = h_prime - q*h;
v = p_prime - q*p;

if u**2 + v**2 < s:
s = u**2 + v**2
h_prime = h;
h = u;
p_prime = p;
p = v;

u = u - h;
v = v - p;

if s = u**2 + v**2:
v_2 = sqrt(s);

