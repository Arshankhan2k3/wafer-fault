
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://arshansince2k3:lXplrkU6H1P1Nq6b@cluster0.q4uzvk4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)