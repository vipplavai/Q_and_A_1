import pymongo
import urllib.parse

# MongoDB Credentials
username = "prashanth01071995"
password = "pradsml@2025"  # Ensure security by replacing this with an environment variable

# Encode special characters in the password
encoded_password = urllib.parse.quote_plus(password)

# MongoDB Connection URI
MONGO_URI = f"mongodb+srv://{username}:{encoded_password}@cluster0.fsbic.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client["Q_and_A"]  # Use actual database name
    collection = db["content_data"]  # Collection name
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
