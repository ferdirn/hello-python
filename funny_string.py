#!/usr/bin/env python

x = int(raw_input())

input = []
rev = []

for i in xrange(x):
    ri = raw_input()
    input.append(ri)
    rev.append(ri[::-1])

def is_funny(a1, a2, b1, b2):
    t1 = abs(ord(a1) - ord(a2))
    t2 = abs(ord(b1) - ord(b2))
    if t1 == t2:
        return 'Funny'
    else:
        return 'Not Funny'

for i in xrange(x):
    res = 'Funny'
    a = input[i]
    b = rev[i]
    for j in xrange(1, len(a)):
        x = is_funny(a[j], a[j-1], b[j], b[j-1])
        print a[j], a[j-1], b[j], b[j-1], x
        if x == 'Not Funny':
            res = 'Not Funny'
            break

    print res

