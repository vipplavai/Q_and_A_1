from flask import Flask, jsonify
from db import db, collection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask App Running!"})

@app.route("/test-db")
def test_db():
    try:
        # Check if we can fetch one document from the database
        data = collection.find_one()
        if data:
            return jsonify({"status": "success", "message": "Connected to MongoDB", "sample_data": data})
        else:
            return jsonify({"status": "success", "message": "Connected, but no data found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
