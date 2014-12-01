#!/usr/bin/env python

def check_level(level):
    if level < 1:
        raise "Invalid level!", level
    else:
        return True;
