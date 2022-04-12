# GPS Translation

## Table of Contents
1. [General Info](#general-info)
1. [Careful](#careful)
2. [Technologies](#technologies)
3. [Installation](#installation)

### General Info
***
This script converts (geocode) GPS coordinates to DMS format (40° 22′ 44″ N, 77° 55′ 56″ W) or decimal (50.1234567, 3.1234567) into postal addresses.
It uses the Open Street Map API.
It requires as input a csv data file with two columns without title:
   >One column with the longitude, one column with the latitude.
   >The separator can be comma, semi-colon, pipe or tab.
   >The two columns must be of the same length.
It returns a file results.csv located in the directory where the script is launched.
The GPS coordinates must be to DMS format (40° 22′ 44″ N, 77° 55′ 56″ W) or decimal (50.1234567, 3.1234567)

### Careful
***
Open street map: https://www.openstreetmap.fr/ is a free cooperative map.
Cooperative means that it is the users who complete this database. It may therefore contain errors.
Please check the information returned by this script before any important use.
I decline any responsibility in case of erroneous results.

## Technologies
***
* [API name](https://www.openstreetmap.fr/)

## Installation
***

'''
$ git clone https://github.com/chpe1/gpsTranslation.git
$ cd ../path/to/the/file
$ pip install --upgrade -r requirements.txt
$ python gps.py -- file mon_fichier_de_donnees.csv
'''
