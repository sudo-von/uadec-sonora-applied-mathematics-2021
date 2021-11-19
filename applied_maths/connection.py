from pymongo import MongoClient

# MongoDB set-up.
def connect(user,password,hostname,port,db_name):
    print("*"*100)
    print("Establishing connection with the database...")
    client = MongoClient(f"mongodb://{user}:{password}@{hostname}:{port}/")
    database = client[db_name]
    print("The connection was successfully established...")
    print("*"*100)
    return database