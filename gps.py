import requests
import csv
import argparse
import re


parser = argparse.ArgumentParser(
    description='Récupération des coordonnées GPS')
parser.add_argument('--file', metavar='-F',
                    help='Fichier contenant les données')
args = parser.parse_args()


def read_csv(file):
    coord = []
    with open(file, 'r') as f:
        my_reader = csv.reader(f)
        for row in my_reader:
            coord.append([row[0], row[1]])
    return coord


def write_csv(liste):
    with open('resultats.csv', 'w', newline='') as ft:
        writer = csv.writer(ft)
        for row in liste:
            # check GPS coordinates format
            if re.match(r'((?:[\+-]?[0-9]*[\.,][0-9]+)|(?:[\+-]?[0-9]+))', row[0]) and re.match(r'((?:[\+-]?[0-9]*[\.,][0-9]+)|(?:[\+-]?[0-9]+))', row[1]):
                payload = {'format': "jsonv2",
                           'lat': row[0], 'lon': row[1], 'zoom': 18, 'addressdetails': 1}
                resp = requests.get(
                    "https://nominatim.openstreetmap.org/reverse?", params=payload)
                print(resp.json()['display_name'])
                writer.writerow([row[0], row[1], resp.json()['display_name']])
            else:
                print("Coordonnées GPS invalides")


# print(read_csv(args.file)
write_csv(read_csv(args.file))
