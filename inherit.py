#!/usr/bin/env python

class Hallo:
    def print_hallo(self):
        print 'Hallo!'

h = Hallo()
h.print_hallo()

class Apakabar(Hallo):
    def print_apa_kabar(self):
        print 'Apa kabar!'

a = Apakabar()
a.print_hallo()
a.print_apa_kabar()
