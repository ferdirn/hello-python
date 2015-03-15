#!/usr/bin/env python

def hitung_luas(alas, tinggi):
    luas = alas * tinggi / 2.
    return luas

print 'Aplikasi untuk menghitung luas segitiga'
alas = int(raw_input('Masukkan alasnya : '))
tinggi = int(raw_input('Masukkan tingginya : '))
luas = hitung_luas(alas, tinggi)
print 'Luasnya adalah ' + str(luas)
