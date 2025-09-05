from dotenv import load_dotenv
import os
import pymongo

# Load env variables
load_dotenv()

# Get the Mongo URI
mongo_uri = os.getenv("MONGO_URI")

# Connects to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client.sample_mflix
collection = db.movies

print(collection.find().limit(5))