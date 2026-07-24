from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi


load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI") # mongodb://localhost:27017/

# Connect to MongoDB server
client = MongoClient(
    mongo_uri,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("MongoDB Atlas Connected Successfully")
except Exception as e:
    print("MongoDB Error:", e)

# Select database
db = client["mydatabase"]

def dbconnect():
    return db