#!/usr/bin/env python

print 'binary of 5 is', bin(5)[2:]
print 'binary of 12 is', bin(12)[2:]

print '5 and 12 is', bin(5&12)[2:]
print '5 or 12 is', bin(5|12)[2:]
print '5 xor 12 is', bin(5^12)[2:]
print 'not 5 is', bin(~5)
print '2 shift left 5 is', bin(5<<2)[2:], ' or ', 5<<2
print '2 shift right 5 is', bin(5>>2)[2:], ' or ', 5>>2
