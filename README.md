# Formation Data Scrapping et Dataviz

Tutoriels, codes sources et données produites lors de la formation Data scrapping et Dataviz [@ANPTIC](http://www.anptic.gov.bf/) de novembre 2015 à Ouagadougou.

## Extraction de données PDF

* 1er TP : [Les tableaux](https://github.com/regardscitoyens/formation-burkina-novembre-2015/raw/master/tofe/Formation_Burkina_Faso_novembre_2015_TP1.odt)

  * Réalisation d'un parseur : [Tableaux des Opérations Financières de l’État](https://github.com/regardscitoyens/formation-burkina-novembre-2015/tree/master/tofe).

* 2ème TP : Les documents textuels

  * Réalisation d'un parseur : Code pénal.

* Données sur les inscrits aux listes éléctorales par bureaux de votes fourni par la CENI

  * Lecture commentée du [parseur](https://github.com/regardscitoyens/formation-burkina-novembre-2015/tree/master/bv_burkina) réalisé par le formateur.

## Dataviz :

[Prise de notes collaboratives avec Etherpad](https://lite6.framapad.org/p/TP_Dataviz_Burkina_11_2015).

  * Panorama des différents outils existants avec un peu de théorie sur les types de graphiques et leur adéquation avec le type de données étudiées.

  * Collecte de données à plusieurs sur la population par provinces pour créer un fichier CSV manuellement.

  * Mise en pratique :

    * Utilisation de [RAW](http://raw.densitydesign.org/) avec les données population précédemment collectées.

    * Atelier cartographie avec [CartoDB](https://cartodb.com/) :

      * Réalisation d'une [carte du nombre d'inscrits](https://popeye.cartodb.com/viz/8c739bde-93ce-11e5-8a2c-0ef7f98ade21/public_map) sur les listes électorales par provinces (fichier SHP fourni).

      * Réalisation d'une carte de la population par provinces en enrichissant le fichier SHP avec le fichier CSV précédemment créé (utilisation de l'outil d'appariement de CartoDB).

## [Scrapping de sites web](https://github.com/regardscitoyens/formation-burkina-novembre-2015/tree/master/juriscrapper) :

  * TP : [Les Jurisprudences Burkinabées du site Juricaf.org](https://github.com/regardscitoyens/formation-burkina-novembre-2015/raw/master/juriscrapper/Formation_Burkina_Faso_novembre_2015_TP3.odt)

## Données résultantes :
  * [Tableaux des Opérations Financières de l'Etat (TOFE) de 2007 à 2012](https://github.com/regardscitoyens/formation-burkina-novembre-2015/tree/master/tofe/csv)
  * Code Pénal
  * [Bureaux de votes et inscrits](https://raw.githubusercontent.com/regardscitoyens/formation-burkina-novembre-2015/master/bv_burkina/bv_clean.csv)
  * [Population 2006](https://github.com/regardscitoyens/formation-burkina-novembre-2015/raw/master/population/population_burkina_2006.csv)
  * [Fichiers SHP des provinces](https://github.com/regardscitoyens/formation-burkina-novembre-2015/tree/master/dataviz/provinces_burkina)
  * Jurisprudences
    * [Burkina Faso (283)](https://github.com/regardscitoyens/formation-burkina-novembre-2015/raw/master/juriscrapper/http-www-juricaf-org-recherche-facet-pays-3aburkina-faso/data.csv)
    * [Bénin (2612)](https://github.com/regardscitoyens/formation-burkina-novembre-2015/raw/master/juriscrapper/http-www-juricaf-org-recherche-facet-pays-3ab-c3-a9nin/data.csv)
