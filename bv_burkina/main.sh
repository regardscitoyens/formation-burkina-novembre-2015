#!/bin/bash
echo "Region;Province;Commune;Secteur_Village;Emplacement;Bureau_de_vote;Inscrits" > bv_clean.csv
python parse.py | grep -v Nombre | sed -e 's/; /;/' | sed -e 's/;$//' >> bv_clean.csv
