#!/usr/bin/env python

for i in xrange(1, 51):
    if i%5 == 0 or i%5 == 2:
        print i, '*',
    else:
        print i,
