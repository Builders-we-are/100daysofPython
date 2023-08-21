import json
import pymongo

# MongoDB connection details
mongo_uri = "mongodb://localhost:27017"  # Update with your MongoDB URI
database_name = "your_db_name"  # Update with your database name
collection_name = "your_collection_name"  # Update with your collection name

# Function to load CZML data from a file
def load_czml_data(file_path):
    with open(file_path, "r") as czml_file:
        czml_data = json.load(czml_file)
    return czml_data

# Function to insert CZML data into MongoDB
def insert_czml_data_into_mongodb(czml_data, db_uri, db_name, collection_name):
    client = pymongo.MongoClient(db_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Insert CZML data into the MongoDB collection
    collection.insert_many(czml_data)

    # Close the MongoDB connection
    client.close()

if __name__ == "__main__":
    czml_file_path = "path/to/your.czml"  # Update with the path to your CZML file

    try:
        czml_data = load_czml_data(czml_file_path)
        insert_czml_data_into_mongodb(czml_data, mongo_uri, database_name, collection_name)
        print("CZML data successfully inserted into MongoDB.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
