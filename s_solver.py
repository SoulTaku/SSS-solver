#!/usr/bin/python
from z3 import *

s = Solver()

k = int(raw_input('Threshold: '))
f = raw_input('File name: ')

shares = open(f, 'r').read().split()

X = [Int('x{}'.format(int(i+1))) for i in range(k)]

base_eq = '{}X[{}] * {}'

for share in shares:
	nr, share = share.split('-')
	nr = int(nr)

	i = 0
	eq = base_eq.format('', i, 1)
	for i in range(k-1):
		i += 1
		eq += base_eq.format(' + ', i, nr**i)
	eq += ' == {}'.format(share)
	
	try:
		s.add(eval(eq))
	except:
		for i in range(len(shares)):
			print(X[i])

# print(s)
assert s.check() == sat
print(s.model()[X[0]])
	
