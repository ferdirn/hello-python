#!/usr/bin/env python

import math
print 'Aplikasi untuk menghitung luas lingkaran'
jari_jari = int(raw_input('Masukkan jari-jari : '))
power = jari_jari ** 2
luas = math.pi * power
print 'Luas lingkarannya = ' + str(luas)
