#!/bin/bash

## TELECHARGEMENT

# Faire un slug de l'url pour nommer le dossier qui contiendra son résultat
directory="$(echo -n $1 | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)"

if [ -d "./$directory" ]; then
  rm -r "./$directory" ;
fi

mkdir -p "./$directory/results"
mkdir -p "./$directory/files"

# Télécharger la page de résultats initiale
wget $1 -O "./$directory/init.html" -q -U "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0" --header="Accept-Language: en-us,en;q=0.5" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" --header="Connection: keep-alive" --referer="/"

# Obtenir la liste des urls des pages de résultats
python getResults.py "./$directory/init.html" > "./$directory/results/results.txt"

# Télécharger les pages de résultats et les stocker dans le dossier "results"
cd "./$directory/results"
wget -i ./results.txt --wait 1 --random-wait -q -U "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0" --header="Accept-Language: en-us,en;q=0.5" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" --header="Connection: keep-alive" --referer="/"

# Obtenir la liste des urls des fichiers à télécharger
cd ../../
> "./$directory/files/files.txt"
for file in $(find "$directory/results/" -name "*page*") ; do python getLinks.py "$file" >> "./$directory/files/files.txt" ; done

# Télécharger les fichiers pour les stocker dans le dossier "files"
cd "./$directory/files"
wget -i ./files.txt --wait 1 --random-wait -q -U "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0" --header="Accept-Language: en-us,en;q=0.5" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" --header="Connection: keep-alive" --referer="/"

## EXTRACTION DES DONNÉES

# Test des variables
cd ../../
> "./$directory/check.csv"
for file in $(find "$directory/files/" -name "*-*") ; do python checkVars.py "$file" >> "./$directory/check.csv" ; done

# Détermination des colonnes
python extractHeader.py "./$directory/check.csv" > "./$directory/header.csv"

# Parser les fichiers et stocker les résultats dans data.csv
cat "./$directory/header.csv" > "./$directory/data.csv"
for file in $(find "$directory/files/" -name "*-*") ; do python parser.py "$file" >> "./$directory/data.csv" ; done
