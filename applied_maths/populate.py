import pandas

def populate_collection_by_file_path(collection, file_path):
    print("*"*100)
    print("Checking if the collection can be populated...")
    # Checks if there are documents stored.
    stored_documents = collection.count_documents({})
    if stored_documents > 0:
        print("Collection already populated.")
        print("*"*100)
        return

    # Reads csv.
    csv = pandas.read_csv(file_path)
    # Gets csv columns.
    print("Cleaning data...")
    data_frame = pandas.DataFrame(csv)
    data_frame["latitud"] = data_frame["latitud"].str.replace(',', '.', 1).astype(float) 
    data_frame["longitud"] = data_frame["longitud"].str.replace(',', '.', 1).astype(float) 
    data_frame["fecha_hora"] = pandas.to_datetime(data_frame['fecha_hora'], format="%Y-%m-%d %H:%M:%S")
    data_frame["tp"] = data_frame["tp"].str.replace(',', '.').astype(float) 
    data_frame["tmax"] = data_frame["tmax"].str.replace(',', '.').astype(float)
    data_frame["tmin"] = data_frame["tmin"].str.replace(',', '.').astype(float) 
    data_frame["hr"] = data_frame["hr"].str.replace(',', '.').astype(float) 
    data_frame["precip"] = data_frame["precip"].str.replace(',', '.').astype(float) 
    data_frame["vv"] = data_frame["vv"].str.replace(',', '.').astype(float) 
    data_frame["dv"] = data_frame["dv"].str.replace(',', '.').astype(float) 
    data_frame["rs"] = data_frame["rs"].str.replace(',', '.').astype(float) 
    data_frame["pb"] = data_frame["pb"].str.replace(',', '.').astype(float) 
    # Inserts all records.
    records = data_frame.to_dict('records')
    collection.insert_many(records)
    print(f"Inserted {len(records)} documents...")
    print("*"*100)