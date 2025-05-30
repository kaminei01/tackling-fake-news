from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb://localhost:27017/")
db = client["fakenews_db"]
collection = db["results"]


def save_result(data):
    result = collection.insert_one(data)
    data["_id"] = str(result.inserted_id) 
    return data

def get_recent_results(limit=10):
    results = list(collection.find().sort("_id", -1).limit(limit))
    for result in results:
        result["_id"] = str(result["_id"])  # Convert ObjectId to string
    return results