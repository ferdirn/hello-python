#!/usr/bin/env python

try:
    fh = open("nofile.txt", "r")
except IOError, e:
    print "Error nih"
    print str(e)
else:
    print "Success"
    fh.close()
finally:
    print "End"
