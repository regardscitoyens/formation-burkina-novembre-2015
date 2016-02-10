#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, urlparse
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(sys.argv[1]), "html5lib")

for link in soup.find_all('a'):
  if link.get_text() == 'Fin >>':
    path = urlparse.urlparse(link.get('href'))
    params = urlparse.parse_qs(urlparse.urlparse(link.get('href')).query)
    nbpages = int(params['page'][0])

prefix = "http://www.juricaf.org"+path.path

for i in range(nbpages):
  print(prefix+'?page='+str(i+1))
