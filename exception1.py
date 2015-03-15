#!/usr/bin/env python

print 'Aplikasi buka file dengan try except'

try:
    fh = open('exception1.txt', 'w')
    fh.write('This is my test file for exception handling!')
except IOError:
    print 'Error: can\'t find file or read data'
else:
    print 'Written content in the file successfully'
    fh.close()
