#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, io, csv, re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(sys.argv[1]), "lxml-xml")

data = {
  'title': 'title',
  'caseref': 'caseref',
  'content': 'content'
}

# On teste les variables DC
for meta in soup.find_all('meta'):
  if str(meta.get('name')).startswith("DC"):
    data[meta.get('name')] = meta.get('name')

# Formatage CSV
output = io.BytesIO()
writer = csv.DictWriter(output, fieldnames=sorted(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
writer.writerow({k:v.encode('utf8') for k,v in data.items()})
print(output.getvalue().strip())
