# gpsTranslation
Ce script convertit (géocode) des coordonnées GPS en adresses postales.
Il utilise l'API Open Street Map.
Il nécessite un fichier de données csv de deux colonnes sans titre:
   Une colonne avec la longitude, une colonne avec la latitude.
Il retourne un fichier csv.

Utilisation :

python gps.py -- file mon_fichier_de_donnees.csv