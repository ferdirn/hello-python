#!/usr/bin/env python

max_redeem = int(raw_input('max_redeem='))
used_counter = int(raw_input('used_counter='))

def is_available(max_redeem, used_counter):
    return True if max_redeem == 0 or max_redeem > used_counter else False

print is_available(max_redeem, used_counter)

