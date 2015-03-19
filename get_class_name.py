#!/usr/bin/env python

class Person():

    def __unicode__(self):
        return self.__class__.__name__

    def get_name(self):
        return self.__class__.__name__

person = Person()

print person

print person.get_name()

print person.__doc__

print person.__module__

print dir(person)

print type(person)

print __name__

