#!/usr/bin/env python

from collections import OrderedDict

# regular unsorted dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

print OrderedDict(sorted(d.items(), key=lambda t: t[1]))


