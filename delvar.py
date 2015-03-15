#!/usr/bin/env python

a = 10
b = 15

print a
print b

print 'delete variable a'
del a

if 'a' in locals():
    print a
else:
    print 'variable a not exists'

print b

print 'print locals()'
print locals()

print 'print globals()'
print globals()

print 'print this filename'
print __file__
