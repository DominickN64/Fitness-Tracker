'''from flask import Flask
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
import certifi



MONGO_URI = os.getenv("MONGO_URI")



ca_cert_path = certifi.where()

cluster = MongoClient(MONGO_URI,tlsCAFile=ca_cert_path)

db = cluster["FitnessApp"]
collection = db["UserInfo"]

collection.insert_one({
    "_id":21,
    "name":"Jack Black"
})

result = collection.find_one({"name": "Jack Black"})

if result:
    print("Found a document:", result['_id'])
else:
    print("No document matches the query.")'''