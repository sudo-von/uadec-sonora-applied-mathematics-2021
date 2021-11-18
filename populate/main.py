import pymongo
import pandas
import os
from pymongo import MongoClient

# Mongo set-up.
client = MongoClient("mongodb://root:root@mongo:27017/")
database = client["database"]
collection = database["remas"]

stored_documents = collection.count_documents({})
if stored_documents > 0:
    quit()

path = './data/BLOCK_419.csv'
# Read csv.
csv = pandas.read_csv(path)
# Get csv columns.
data_frame = pandas.DataFrame(csv)
data_frame["latitud"] = data_frame["latitud"].str.replace(',', '.', 1).astype(float) 
data_frame["longitud"] = data_frame["longitud"].str.replace(',', '.', 1).astype(float) 
data_frame["tp"] = data_frame["tp"].str.replace(',', '.').astype(float) 
data_frame["tmax"] = data_frame["tmax"].str.replace(',', '.').astype(float)
data_frame["tmin"] = data_frame["tmin"].str.replace(',', '.').astype(float) 
data_frame["hr"] = data_frame["hr"].str.replace(',', '.').astype(float) 
data_frame["precip"] = data_frame["precip"].str.replace(',', '.').astype(float) 
data_frame["vv"] = data_frame["vv"].str.replace(',', '.').astype(float) 
data_frame["dv"] = data_frame["dv"].str.replace(',', '.').astype(float) 
data_frame["rs"] = data_frame["rs"].str.replace(',', '.').astype(float) 
data_frame["pb"] = data_frame["pb"].str.replace(',', '.').astype(float) 
# Insert all records.
collection.insert_many(data_frame.to_dict('records'))
print("already populated")