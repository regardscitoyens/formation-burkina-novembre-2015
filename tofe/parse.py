#!/usr/bin/env python
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("tofe.xml"), "lxml-xml")
#soup = BeautifulSoup(open("tofe.xml"), "html.parser")

data = {}

# Récupérer et stocker les données dans "data"

for page in soup.find_all('page'):

  pgnb = int(page.get('number'))

  data[pgnb] = {}

  for text in page.find_all('text'):

    top = int(text.get('top'))

    if data[pgnb].has_key(top) is False:
      data[pgnb][top] = {}

    left = int(text.get('left'))

    data[pgnb][top][left] = text.get_text()

# Trier et afficher les données

sorted_data = sorted(data)

for page in sorted_data:

  sorted_page = sorted(data[page])

  for line in sorted_page:

    sorted_line = sorted(data[page][line])

    csv = ''

    for cel in sorted_line:

      csv += data[page][line][cel]+';'

    csv.rstrip(';')

    print(csv.encode('utf-8'))
