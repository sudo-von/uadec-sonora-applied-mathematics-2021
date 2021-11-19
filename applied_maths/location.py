import os
import pprint
import reverse_geocoder
import pandas

def get_recursive_locations(folder):
    print("*"*100)
    print(f"Getting locations from each file given the folder {folder}...")
    # Gets path for each file in the given folder.
    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            # Reads each file and then get coordinates.
            coordinates = get_coordinates(path)
            location = reverse_geocoder.search(coordinates)
            print(location)
    print("*"*100)

def get_coordinates(path):
    # Stores data as str because we will use str methods.
    csv = pandas.read_csv(path, dtype=str)
    data_frame = pandas.DataFrame(csv, columns= ['latitud','longitud'])
    for index, row in data_frame.iterrows():
        # Data clean.
        latitude = row['latitud'].replace(',','.')
        longitude = row['longitud'].replace(',','.')
        coordinates = (latitude, longitude)
        return coordinates
