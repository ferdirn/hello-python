#!/usr/bin/env python

print 'App temp convert'

var = raw_input('Masukkan suatu angka: ')

def temp_convert(var):
    try:
        result = int(var)
    except ValueError, Argument:
        print 'The argument is not a number\n', Argument
    else:
        print str(var) + ' is a number'
	return result

temp_convert(var)
