#!/usr/bin/env python

import requests

html_doc = requests.get('http://www.hitunghuruf.com')

print html_doc.status_code
print html_doc.headers
print html_doc.content
