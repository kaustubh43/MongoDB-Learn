import datetime
import certifi
from pymongo import MongoClient
import os

ca = certifi.where()  # Certificate
password = os.environ['APP_PASSWORD']  # Take password from environment variable
cluster = f"mongodb+srv://kaustubh43:{password}@cluster1.au46pco.mongodb.net/?retryWrites=true&w=majority"
# Database name = todo_application
# Collection name = todo

client = MongoClient(cluster, tlsCAFile=ca)  # Connect to database

db = client.todo_application
# print database names
# print(db.list_database_names())

sample = {"name": "Kaustubh",
          "text": "My first TEXT",
          "status": "open",
          "tags": ["python", "coding", "python-programming-language"],
          "date": datetime.datetime.utcnow()}

todo_temp = db.todo
print(type(db.todo))

result = todo_temp.insert_one(sample)
