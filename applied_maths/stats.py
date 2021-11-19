def search_anomalous_temperatures(collection, tmin, tmax):
    print("*"*100)
    print("Searching for anomalous temperatures...")
    tmin_result = collection.count_documents({ "tmin": { "$lt" : tmin } })
    tmax_result = collection.count_documents({ "tmax": { "$gt" : tmax  } })
    print(f"Number of rows where tmin are less than {tmin}: {tmin_result} rows.")
    print(f"Number of rows where tmax are greater than {tmax}: {tmax_result} rows.")
    print("*"*100)