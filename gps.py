import requests
import csv
import argparse
import re


parser = argparse.ArgumentParser(
    description='Imported GPS coordinates in decimal or DMS format')
parser.add_argument('--file', metavar='-F',
                    help='File containing the data', required=True)
args = parser.parse_args()

# 48° 51′ 29″ N
lat_DMS = re.compile(
    r'[\+-]?(([1-8]?\d)\D+([1-5]?\d|60)\D+([1-5]?\d|60)(\.\d+)?|90\D+0\D+0)\D+[NSns]?')
# 02° 17′ 40″ E
lng_DMS = re.compile(
    r'[\+-]?([1-7]?\d{1,2}\D+([1-5]?\d|60)\D+([1-5]?\d|60)(\.\d+)?|180\D+0\D+0)\D+[EWew]?')
# 48.8583306
lat_DECIMAL = re.compile(r'^(-?[1-8]?\d(?:\.\d{1,18})?|90(?:\.0{1,18})?)$')
# 2.29451111
lng_DECIMAL = re.compile(
    r'^((-?(?:1[0-7]|[1-9])?\d(?:\.\d{1,18})?|180(?:\.0{1,18})?))$')


def find_separator(file):
    """
        Find the separator of the file
    """
    with open(file, 'r', encoding="utf-8") as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        return dialect.delimiter


def convert_dmstodecimal(coordonnees_gps):
    """
        Convert DMS format to decimal degree format
    """
    direction = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
    new = ''
    for i in coordonnees_gps:
        if i.isdigit():
            new += i
        elif i in direction:
            new += i
        else:
            new += ' '
    new = new.split()
    new_dir = new.pop()
    if new[3] is not None:
        new[2] = str(new[2]) + '.' + str((new[3]))
        del new[3]
    return (int(new[0])+int(new[1])/60.0+float(new[2])/3600.0) * direction[new_dir]


def read_csv(file, separator):
    coord = []
    with open(file, 'r', encoding="utf-8") as f:
        my_reader = csv.reader(f, delimiter=separator)
        for row in my_reader:
            # check if GPS coordinates is decimal format
            if re.match(lat_DECIMAL, row[0]) and re.match(lng_DECIMAL, row[1]):
                coord.append([row[0], row[1]])
            # check if GPS coordinates is DMS format
            elif re.match(lat_DMS, row[0]) and re.match(lng_DMS, row[1]):
                coord.append([convert_dmstodecimal(row[0]),
                             convert_dmstodecimal(row[1])])
            # return error if coordinates are not in DMS or decimal format
            else:
                return "This script only works with decimal or DMS format"
    return coord


def write_csv(liste):
    """
        Write coordinates in csv file where the name is results.csv
    """
    with open('results.csv', 'w', newline='', encoding="utf-8") as ft:
        writer = csv.writer(ft)
        for row in liste:
            payload = {'format': "jsonv2",
                       'lat': row[0], 'lon': row[1], 'zoom': 18, 'addressdetails': 1}
            resp = requests.get(
                "https://nominatim.openstreetmap.org/reverse?", params=payload)
            print(resp.json()['display_name'])
            writer.writerow([row[0], row[1], resp.json()['display_name']])
    print("File results.csv generated with success")


sep = find_separator(args.file)
write_csv(read_csv(args.file, sep))
