"""
This script converts (geocode) GPS coordinates into postal addresses.
It uses the Open Street Map API.
It requires as input a csv data file with two columns without title:
   One column with the longitude, one column with the latitude.
   The separator is the comma.
   The two columns must be of the same length.
It returns a file results.csv located in the directory where the script is launched.
The GPS coordinates must be in the form 50.12345,4.12345

Usage :

pip install --upgrade -r requirements.txt
python gps.py -- file mon_fichier_de_donnees.csv


"""
import requests
import csv
import argparse


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
