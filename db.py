# db.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gir:1@cluster0.ajxxi2q.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

if __name__ == '__db__':
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
