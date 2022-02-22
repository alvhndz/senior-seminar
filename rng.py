#rng.py
import numlib
import random

def rng():
	rn= random.randint(80,350)
	return rn

for i in range(40):
	print(rng())
