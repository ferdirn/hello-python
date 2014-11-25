#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

result = requests.get('http://google.com/search?q=bor+listrik')
html = result.content

soup = BeautifulSoup(html)

links = soup.find_all('a')

for l in links:
    print l

print len(links)
