#!/usr/bin/env python

a = 1
b = 2
print 'a = ', a
print 'b = ', b
print '\n'

#ternary operator
print 'Ternary operator #1'
print 'a > b' if (a > b) else 'b > a'

print '\nTernary operator #2'
print (a > b) and 'a > b' or 'b > a'
