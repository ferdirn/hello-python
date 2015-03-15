#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', default=0, help='an integer from the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
    help='sum the integers (default: find the max)')
parser.add_argument('--reverse', metavar='A', dest='reverse', nargs=2,
    help='reverse the first 2 argument')

args = parser.parse_args()
print args
