#!/usr/bin/env python

nama_hari = raw_input('Masukkan nama hari : ')

if nama_hari == 'sabtu' or nama_hari == 'minggu':
    print 'Weekends'
elif nama_hari == 'senin' or nama_hari == 'selasa' or nama_hari == 'rabu' or nama_hari == 'kamis':
    print 'Weekdays'
elif nama_hari == "jum'at":
    print 'TGIF'
else:
    print 'Nama hari tidak dikenal'
