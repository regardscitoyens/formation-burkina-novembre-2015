#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, io, csv

reader = csv.reader(open(sys.argv[1], 'r'))

data = {}

for row in reader:
  for val in row:
    data[val] = val

# Formatage CSV
output = io.BytesIO()
writer = csv.DictWriter(output, fieldnames=sorted(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
writer.writerow({k:v.encode('utf8') for k,v in data.items()})
print(output.getvalue().strip())
