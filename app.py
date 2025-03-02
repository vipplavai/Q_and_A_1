from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pymongo
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load MongoDB URI from Environment Variables
MONGO_URI = os.getenv("MONGO_URI")

try:
    if not MONGO_URI:
        raise Exception("MONGO_URI is missing! Set it in Render Environment Variables.")

    client = pymongo.MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000,
        tls=True,  # Ensure TLS connection
        tlsAllowInvalidCertificates=True  # Temporary fix for Render SSL issues
    )
    db = client["Q_and_A"]
    collection = db["content_data"]
    client.admin.command('ping')  # Test connection
    print("✅ Connected to MongoDB Successfully!")
except Exception as e:
    print(f"❌ MongoDB Connection Failed! Error: {e}")

@app.route('/')
def home():
    try:
        return jsonify({"status": "success", "message": "Flask MongoDB is working!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Ensure Render uses correct PORT
    app.run(host='0.0.0.0', port=port, debug=True)
