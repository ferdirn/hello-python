#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    a = int(sys.argv[1])
else:
    a = 1

if a > 0:
    print 'True'
else:
    print 'False'
