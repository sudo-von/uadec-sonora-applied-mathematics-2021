import pymongo
import pandas
import os
from pymongo import MongoClient

# Mongo set-up.
client = MongoClient("mongodb://root:root@mongo:27017/")
database = client["database"]
collection = database["remas"]

tmin = collection.count_documents({ "tmin": { "$lt" : -10 } })
tmax = collection.count_documents({ "tmax": { "$gt" : 50 } })

print("Number of rows where tminx are less than -10: {} rows.".format(tmin))
print("Number of rows where tmax are bigger than 50: {} rows.".format(tmax))