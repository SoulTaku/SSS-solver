#!/usr/bin/python2
from lagrange import Lagrange

file = raw_input('File: ')
shares = open(file, 'r').read().split()

xs = [int(i.split('-')[0]) for i in shares]
ys = [int(i.split('-')[1]) for i in shares]

print(Lagrange(xs, ys).interpolate())

