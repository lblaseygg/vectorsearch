import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# Load env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["movie_recs"]
collection = db["movies"]

# Load Hugging Face Model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Insert Movies with embeddings
movies = [
    {"title": "Interstellar", "description": "A team travels through a wormhole in space."},
    {"title": "Inception", "description": "A thief steals secrets through dream-sharing technology."},
    {"title": "The Matrix", "description": "A hacker discovers reality is a simulation."}
]
