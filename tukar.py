#!/usr/bin/env python

import sys

if len(sys.argv) > 2:
    sys.argv[1], sys.argv[2] = sys.argv[2], sys.argv[1]
    print sys.argv[1], sys.argv[2]
else:
    print 0
