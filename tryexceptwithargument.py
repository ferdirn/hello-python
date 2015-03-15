#!/usr/bin/env python

print 'App try except with argument'

try:
    fh = open ('testfile', 'r')
except IOError, Argument:
    print 'Can\'t open file!\n', Argument
else:
    print 'Open file successfully!'
    fh.close()
