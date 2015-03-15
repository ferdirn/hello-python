#!/usr/bin/env python

try:
    fh = open("exception.txt", "w")
    fh.write("this is a exception test")
except IOError, e:
    print str(e)
else:
    print "Success"
    fh.close()
