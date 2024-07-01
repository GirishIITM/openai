from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# User schema
user_schema = {
    'name': 'string',
    'password': 'string',
    'email': 'string',
    'username': 'string'
}
