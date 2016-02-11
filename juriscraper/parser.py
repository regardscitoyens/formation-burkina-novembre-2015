#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, io, csv, re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(sys.argv[1]), "lxml-xml")

# Initialiser un dictionnaire basé sur header.csv pour recueillir les données
directory = re.sub(r"/.+", "", sys.argv[1])
reader = csv.reader(open(directory+'/header.csv', 'r'))
data = {}

for row in reader:
  for val in row:
    data[val] = ''

# Métas Dublin Core
for meta in soup.find_all('meta'):
  if str(meta.get('name')).startswith("DC"):
    data[meta.get('name')] = meta.get('content')

# Titre
data['title'] = soup.title.string

# Numéro d'affaire
data['caseref'] = data['title'].split(',')[-1].strip()

# Texte de la décision
texte = soup.find_all("span", itemprop="articleBody")[0].get_text()

# Suppression des espaces inutiles
texte = re.sub(' {2,}',' ', texte)

# Aérons un peu le texte
texte = re.sub('\n','\n\n', texte)

data['content'] = texte

# Formatage CSV
output = io.BytesIO()
writer = csv.DictWriter(output, fieldnames=sorted(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
writer.writerow({k:v.encode('utf8') for k,v in data.items()})
print(output.getvalue().strip())
