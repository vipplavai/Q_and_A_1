from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pymongo
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load MongoDB URI from Environment Variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://prashanth01071995:pradsml%402025@cluster0.fsbic.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

try:
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, tls=True, tlsAllowInvalidCertificates=True)
    db = client["Q_and_A"]
    collection = db["content_data"]
    client.admin.command('ping')  # Test Connection
    print("✅ Connected to MongoDB Successfully!")
except Exception as e:
    print(f"❌ MongoDB Connection Failed! Error: {e}")

# Homepage (Fetch Content by ID)
@app.route('/', methods=['GET', 'POST'])
def index():
    content_data = None
    content_id = ""

    if request.method == 'POST':
        content_id = request.form.get("content_id")
        content_data = collection.find_one({"content_id": content_id}, {"_id": 0})

        if not content_data:
            flash("❌ No content found for this ID!", "danger")
    
    return render_template('index.html', content=content_data, content_id=content_id)

# Add Question to Content
@app.route('/add_question', methods=['POST'])
def add_question():
    content_id = request.form.get("content_id")
    question_text = request.form.get("question")
    difficulty = request.form.get("difficulty", "medium")

    if not content_id or not question_text:
        flash("⚠️ Content ID and Question are required!", "danger")
        return redirect(url_for('index'))

    collection.update_one(
        {"content_id": content_id},
        {"$push": {"questions": {"question": question_text, "difficulty": difficulty, "answer": ""}}},
        upsert=True
    )
    
    flash("✅ Question added successfully!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
