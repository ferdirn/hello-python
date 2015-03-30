#!/usr/bin/env python

import requests

r = requests.get('http://www.valadoo.com/api/v3/competitions/tbl/report')

print 'status_code', r.status_code
print 'headers', r.headers
print 'encoding', r.encoding
print 'text', r.text
print 'json', r.json()

