from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["fakenews_db"]

# Updated JSON Schema with reason, tags, and source_type
result_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["claim", "verdict", "confidence"],
        "properties": {
            "claim": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "verdict": {
                "enum": ["FAKE", "REAL"],
                "description": "can only be FAKE or REAL and is required"
            },
            "confidence": {
                "bsonType": ["double", "int"],
                "minimum": 0,
                "maximum": 1,
                "description": "must be a number between 0 and 1 and is required"
            },
            "reason": {
                "bsonType": "string",
                "description": "explanation for the verdict"
            },
            "source_type": {
                "bsonType": "string",
                "description": "type of source: blog, news site, etc."
            },
            "tags": {
                "bsonType": "array",
                "items": {
                    "bsonType": "string"
                },
                "description": "array of relevant tags"
            }
        }
    }
}

try:
    collection = db.create_collection(
        "results",
        validator=result_schema,
        validationLevel="strict"
    )
except CollectionInvalid:
    collection = db["results"]

def save_result(data):
    result = collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data

def get_recent_results(limit=10):
    results = list(collection.find().sort("_id", -1).limit(limit))
    for result in results:
        result["_id"] = str(result["_id"])
    return results
