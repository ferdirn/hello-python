#!/usr/bin/env python

class Person():
    name = 'Ferdi Ramdhon'
    def say(self, what):
        print(self.name, what)

print getattr(Person, 'name')

attr_name = 'name'
person = Person()
print getattr(person, attr_name)

getattr(person, 'say')('helooo...')

g = getattr(person, 'say')('hellooo...')

print type(g)

