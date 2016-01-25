#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, os, re

dirpath = os.path.dirname(os.path.abspath(__file__))

data = open(os.path.join(dirpath, 'bv.csv'))

region = ''
province = ''
commune = ''

reg_region = '^REGION'
reg_province = '^PROVINCE'
reg_commune = '^COMMUNE'

next_com = False

for line in data:

  if re.search(reg_region, line.strip()):
    region = line.strip().split(';')[1]

  if re.search(reg_province, line.strip()):
    province = line.strip().split(';')[1]

  if next_com is True:
    commune = line.strip().split(';')[0]
    next_com = False

  if re.search(reg_commune, line.strip()):
    next_com = True


  if len(line.split(';')) == 5:
    print(region+';'+province+';'+commune+';'+line.strip())
