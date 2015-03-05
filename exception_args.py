#!/usr/bin/env python

try:
    fh = open("nofile.txt", "r")
except IOError, e:
    print "Error nih"
    print e.args
else:
    print "Success"
    fh.close()
finally:
    print "End"
