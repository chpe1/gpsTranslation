# gpsTranslation
Ce script convertit (géocode) des coordonnées GPS en adresses postales.
Il utilise l'API Open Street Map.
Il nécessite en entrée un fichier de données csv de deux colonnes sans titre:
   Une colonne avec la longitude, une colonne avec la latitude.
   Le séparateur est la virgule.
Il retourne un fichier csv.
Les coordonnées GPS doivent être sous la forme 50.12345 4.12345


Open street map : https://www.openstreetmap.fr/ est une carte coopérative libre.
Coopérative signifie que ceux sont les utilisateurs qui complète cette base de données. Elle peut donc contenir des erreurs.
Merci de vérifier les informations retournées par ce script avant toute utilisation importante.

Utilisation :

python gps.py -- file mon_fichier_de_donnees.csv
