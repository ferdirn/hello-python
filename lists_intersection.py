#!/usr/bin/env python

a = [1,2,3]
b = [2]

print "List Intersection"
print "List a", a
print "List b", b
print
i = list(set(a) & set(b))
print "Intersection 1", i
ii = [val for val in a if val in b]
print "Intersection 2", ii

