from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fakenews_db"]
feedback_collection = db["feedback"]

def save_feedback(data):
    feedback_collection.insert_one(data)
