#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

result = requests.get('http://hitunghuruf.com')
html = result.content

soup = BeautifulSoup(html)

links = soup.find_all('a')

for l in links:
    print l
