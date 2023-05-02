import certifi
# import pymongo
from pymongo import MongoClient
import os
ca = certifi.where()
password = os.environ['APP_PASSWORD']
uri = "mongodb+srv://kaustubhajgaonkar43:"+password+"@formsubmissions.ko4j1rf.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri,  tlsCAFile=ca)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
