#!/usr/bin/env python

print 'Exception 2\n'

try:
    f = open('testfile', 'r')
except IOError:
    print 'Can\'t find or open file'
else:
    print 'Open file successfully'
    f.close()
