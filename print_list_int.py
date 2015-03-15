#!/usr/bin/env python

mylist = [11, 22, 33, 44, 55]

print 'mylist'
print mylist

print 'mylist as string'
print str(mylist)

print 'mylist strip square brackets'
print str(mylist).strip('[]')

print 'mylist index 1:-1'
print str(mylist)[1:-1]

print 'map mylist to str, join with newline'
print '\n'.join(map(str, mylist))
