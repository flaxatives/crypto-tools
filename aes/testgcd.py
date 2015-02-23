#!/usr/bin/python

import gcd

a = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
b = [1, 1, 0, 0, 1]

print('Finding gcd of:')
print(gcd.prettify(a) + ' and ' + gcd.prettify(b))

d, g, h, a1, b1 = gcd.extgcd(a,b)
print('d(x) = ' + gcd.prettify(d))
print('g(x) = ' + gcd.prettify(g))
print('h(x) = ' + gcd.prettify(h))
