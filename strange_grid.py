#!/usr/bin/env python

input = raw_input()
r = int(input[:input.find(' ')])
c = int(input[input.find(' ')+1:])

level = (r-1)/2
option = (r-1)%2
answer = (level * 10) + (c * 2) - (2 - option)

print answer

