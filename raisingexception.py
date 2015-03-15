#!/usr/bin/env python

class LevelError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def check_level(level):
    if level < 1:
        raise LevelError('Invalid Level')
    else:
        return True

level = 0

try:
    check_level(level)
except LevelError, e:
    print e
else:
    print "Go to level " + str(level)
