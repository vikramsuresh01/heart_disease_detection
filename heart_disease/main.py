from fastapi import FastAPI
app = FastAPI()

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://vs7552:heart@heartdata.qs1nszn.mongodb.net/?retryWrites=true&w=majority&appName=heartdata"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)