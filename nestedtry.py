#!/usr/bin/env python

print 'App nested try'
try:
    fh = open('testfile.txt', 'w')
    try:
        fh.write('This is my test file for writing exception')
    finally:
        print 'Going to close the file'
	fh.close()
except IOError:
    print 'Can\'t open file'
