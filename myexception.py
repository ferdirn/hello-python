#!/usr/bin/env python

class MyException(Exception):
    """Documentation"""

try:
    raise MyException('An exception')
except MyException as my:
    print my


