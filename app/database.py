from pymongo import MongoClient
import mongomock
import os
import certifi

db = None
collection = None

def init_db(app):
    global db, collection
    if app.config['TESTING']:
        
        cluster = mongomock.MongoClient()
    else:
        
        MONGO_URI = os.getenv("MONGO_URI")
        ca_cert_path = certifi.where()
        cluster = MongoClient(MONGO_URI, tlsCAFile=ca_cert_path)

    db = cluster["FitnessApp"]
    collection = db["UserInfo"]
