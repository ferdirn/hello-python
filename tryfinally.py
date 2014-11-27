#!/usr/bin/env python

print 'try finally in python\n'

try:
    f = open('testfile', 'r')
except:
    print 'Error: Can\'t open file'
else:
    print 'Entering else'
finally:
    print 'Program done!'

