from pymongo import MongoClient, ASCENDING
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from db import client

user_schema = {
    'name': 'string',
    'password': 'string',
    'email': 'string',
    'username': 'string'
}


# create a user with name girish password 1234 email gir@gmail.com and username gir

def create_user(name, password, email, username):
    db = client['user_db']
    collection = db['users']
    user = {
        'name': name,
        'password': password,
        'email': email,
        'username': username
    }
    collection.insert_one(user)
    
    return user

create_user('girish', '1234', 'gir@gmail.com', 'gir')