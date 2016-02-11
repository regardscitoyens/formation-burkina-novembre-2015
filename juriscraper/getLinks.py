#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, csv, re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(sys.argv[1]), "html5lib")

prefix = 'http://www.juricaf.org'

for link in soup.find_all('a'):
  if link.get('href').startswith('/arret'):
    print(prefix+link.get('href'))
