import time
import os
import csv 
import pprint
import reverse_geocoder as rg
import pandas as pd

def get_location(coordinates):
    result = rg.search(coordinates)
    return result

def read_file(path):
    # Store data as str because we will use str methods.
    csv = pd.read_csv(path, dtype=str)
    data_frame = pd.DataFrame(csv, columns= ['latitud','longitud'])
    for index, row in data_frame.iterrows():
        # Data clean.
        latitude = row['latitud'].replace(',','.')
        longitude = row['longitud'].replace(',','.')
        coordinates = (latitude, longitude)
        location = get_location(coordinates)
        pprint.pprint(location)
        # Go to the next file.
        break

# Get files from folder.
for root, dirs, files in os.walk('./databases'):
    for file in files:
        # Get path for each file.
        path = os.path.join(root, file)
        # Read each file.
        read_file(path)