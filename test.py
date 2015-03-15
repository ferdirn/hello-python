#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    nama_lengkap = ' '.join(sys.argv[1:])
else:
    nama_lengkap = 'Ferdi Ramdhon Nizar'

while(nama_lengkap):
    end_pos = nama_lengkap.find(' ')
    if end_pos < 0:
        print "suku_nama = " + nama_lengkap
	nama_lengkap = None
	break
    print "end_pos = " + str(end_pos)
    suku_nama = nama_lengkap[:end_pos]
    print "suku_nama = " + suku_nama
    nama_lengkap = nama_lengkap[end_pos+1:]
    print "nama_lengkap = " + nama_lengkap

