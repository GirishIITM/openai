from pymongo import MongoClient, ASCENDING
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from db import client

chat_history = {
    'username': 'string',
    'messages': 'Array[string]',
}


def create_chat_history(username):
    db = client['chat_db']
    collection = db['chat_history']
    chat = {
        'username': username,
        'messages': ["this is message 1", "this is message 2", "this is message 3"]
    }
    collection.insert_one(chat)

    return chat

# create_chat_history('girish')

def delete_all_chat_history():
    db = client['chat_db']
    collection = db['chat_history']
    collection.delete_many({})
    return "All chat history deleted"

delete_all_chat_history()