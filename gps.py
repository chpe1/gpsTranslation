"""
Ce script convertit des coordonnées GPS en adresses postales.
Il utilise l'API Open Street Map.
Il nécessite un fichier de données csv de deux colonnes:
   Une colonne avec la longitude, une colonne avec la latitude.

Utilisation :

python gps.py -- file mon_fichier_de_donnees.csv


"""
import requests
import csv
import argparse


# Lecture des arguments de la ligne de commande
parser = argparse.ArgumentParser(
    description='Récupération des coordonnées GPS')
parser.add_argument('--file', metavar='-F',
                    help='Fichier contenant les données')
args = parser.parse_args()


with open(args.file, 'r') as f:
    my_reader = csv.reader(f)
    with open('resultats.csv', 'w') as ft:
        writer = csv.writer(ft)
        for row in my_reader:
            row[1] = row[1].lstrip()
            payload = {'format': "jsonv2",
                       'lat': row[0], 'lon': row[1], 'zoom': 18, 'addressdetails': 1}
            resp = requests.get(
                "https://nominatim.openstreetmap.org/reverse?", params=payload)
            print(resp.json()['display_name'])
            writer.writerow([row[0], row[1], resp.json()['display_name']])
