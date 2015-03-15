#!/usr/bin/env python

t = (1, 2, 3, 4, 5)
print 't = ', t

def check(a):
    if a in t:
        print a, 'in t'
    else:
        print a, 'not in t'

check(3)
check(8)
