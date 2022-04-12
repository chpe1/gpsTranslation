# gpsTranslation
This script converts (geocode) GPS coordinates to DMS format (40° 22′ 44″ N, 77° 55′ 56″ W
) or decimal (50.1234567, 3.1234567) into postal addresses.
It uses the Open Street Map API.
It requires as input a csv data file with two columns without title:
   One column with the longitude, one column with the latitude.
   The separator can be comma, semi-colon, pipe or tab
   The two columns must be of the same length.
It returns a file results.csv located in the directory where the script is launched.
The GPS coordinates must be to DMS format (40° 22′ 44″ N, 77° 55′ 56″ W
) or decimal (50.1234567, 3.1234567)

Open street map: https://www.openstreetmap.fr/ is a free cooperative map.
Cooperative means that it is the users who complete this database. It may therefore contain errors.
Please check the information returned by this script before any important use.
I decline any responsibility in case of erroneous results.

USAGE :

pip install --upgrade -r requirements.txt
python gps.py -- file mon_fichier_de_donnees.csv

------------------------------------------------------------------------------------------------------


Ce script convertit (géocode) des coordonnées GPS au format DMS (40° 22′ 44″ N, 77° 55′ 56″ W
) ou décimal (50.1234567, 3.1234567) en adresses postales.
Il utilise l'API Open Street Map.
Il nécessite en entrée un fichier de données csv de deux colonnes sans titre:
   Une colonne avec la longitude, une colonne avec la latitude.
   Le séparateur peut-être la virgule, le point-virgule, le pipe ou la tabulation
   Les deux colonnes doivent être de même longueur.
Il retourne un fichier results.csv situé dans le répertoire où est lancé le script.
Les coordonnées GPS doivent être au format DMS (40° 22′ 44″ N, 77° 55′ 56″ W
) ou décimal (50.1234567, 3.1234567)


Open street map : https://www.openstreetmap.fr/ est une carte coopérative libre.
Coopérative signifie que ceux sont les utilisateurs qui complètent cette base de données. Elle peut donc contenir des erreurs.
Merci de vérifier les informations retournées par ce script avant toute utilisation importante.
Je décline toute responsabilité en cas de résultats erronés.

Utilisation :

pip install --upgrade -r requirements.txt
python gps.py -- file mon_fichier_de_donnees.csv
