#!/usr/bin/env python

# regular unsorted dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

print d
print sorted(d.items(), key=lambda t: t[1])


