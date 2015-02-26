#!/usr/bin/env python

class BaseClass(object):
    def __init__(self):
        print "I'm base class"

class Child1(BaseClass):
    def __init__(self):
        print "I'm child number 1"
	super(Child1, self).__init__()

c = Child1()
