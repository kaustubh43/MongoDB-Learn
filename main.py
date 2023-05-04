import datetime
import certifi
from pymongo import MongoClient
import os

ca = certifi.where()  # Certificate
password = os.environ['APP_PASSWORD']  # Take password from environment variable
cluster = f"mongodb+srv://kaustubh43:{password}@cluster1.au46pco.mongodb.net/?retryWrites=true&w=majority"
# Database name = todo_application
# Collection name = todo

client = MongoClient(cluster, tlsCAFile=ca)  # Connect to MongoAccount

db = client.todo_application  # connect with Database name

sample = {"name": "Dark-Star",
          "text": "My Second text of day 2",
          "status": "open",
          "tags": ["aviation", "fly"],
          "date": datetime.datetime.utcnow()}

collection_obj = db.todo  # Make a collection object

# result = collection_obj.insert_one(sample)  # Insert one document into collection object using insert_one() function

sample2 = [{"name": "Boeing 747",
            "text": "My testing is ongoing",
            "status": "open",
            "tags": ["aviation", "fly"],
            "date": datetime.datetime.utcnow()},
           {"name": "Airbus A380",
            "text": "My test text",
            "status": "open",
            "tags": ["aviation", "fly"],
            "date": datetime.datetime.utcnow()}
           ]
# result = collection_obj.insert_many(sample2)  # Insert one document into collection object using insert_one() function

# result = collection_obj.find_one()  # Find first item in the collection

# result = collection_obj.find_one({"name": "Kaustubh"})  # Finds specific document, first occurrence in the
# collection only


# result = collection_obj.find_one({"name": "Kaustubh", "text": "My first todo text!"})


# result = collection_obj.find_one({"tags": "java"})  # Find a nested field within an array

# from bson.objectid import ObjectId

# result = collection_obj.find_one({"_id": ObjectId("64528356682f364096b5f2f7")})  # Find by ID
# If you need to find by Object ID then you need ObjectID from bson.objectid

# result = collection_obj.find({"name": "Kaustubh"}) # Find by ID
# print(list(result))  # We can convert the object into a list which will contain the query documents
# Note that this object can be used only once
# for _ in result:
#     print(_)  # or we can iterate over the object and perform actions on it

# print(collection_obj.count_documents({}))  # Counting all documents

# print(collection_obj.count_documents({"name": "Kaustubh"}))  # Counting specific stuff


# Range and Sorting Queries
# d = datetime.datetime(2023, 5, 5)
# result = collection_obj.find({"date": {"$lte": d}}).sort("name")
# print(list(result))
# from bson.objectid import ObjectId

# result = collection_obj.delete_one({"_id": ObjectId("6453caaf2475a9644e558d1f")})  # Deleting by an id

# result = collection_obj.delete_many({"name":"Kaustubh"})  # this will delete many
# If the dictionary is kept empty then it will delete all the documents in the colleciton
# Very powerful operation to do, Use with caution

# result = collection_obj.update_one({"name": "Kaustubh"}, {"$set": {"status": "done"}}) # updates the first occurrence

# result = collection_obj.update_many({"name": "Kaustubh"}, {"$set": {"status": "done"}})  # updates all documents

# result = collection_obj.update_one({"tags": "aviation"}, {"$unset": {"tags": None}})  #  Remove field from a single
# document

# result = collection_obj.update_many({"tags": "aviation"}, {"$unset": {"tags": None}})  # Remove field from all
# matched documents

