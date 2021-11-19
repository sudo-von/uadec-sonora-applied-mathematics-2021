from connection import connect
from populate import populate_collection_by_file_path
from stats import search_anomalous_temperatures
from location import get_recursive_locations

if __name__ == "__main__":
    
    # Database setup.
    database = connect("root","root","mongo","27017","applied_maths")
    collection = database["remas"]
    
    folder_name = "./data"
    file_path = f"{folder_name}/BLOCK_419.csv"
    get_recursive_locations(folder_name)
    populate_collection_by_file_path(collection, file_path)
    search_anomalous_temperatures(collection, -10, 50)