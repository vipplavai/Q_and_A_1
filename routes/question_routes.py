from flask import Blueprint, request, jsonify
from models.db import collection

question_routes = Blueprint("question_routes", __name__)

# Add a New Question
@question_routes.route("/add-question", methods=["POST"])
def add_question():
    data = request.json
    content_id = data.get("content_id")
    question_text = data.get("question")
    difficulty = data.get("difficulty")

    if not content_id or not question_text or not difficulty:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    new_question = {
        "question": question_text,
        "difficulty": difficulty,
        "answer": ""  # Placeholder for answer field
    }

    collection.update_one({"content_id": content_id}, {"$push": {"questions": new_question}})
    return jsonify({"status": "success", "message": "Question added successfully"})

# Edit an Existing Question
@question_routes.route("/edit-question", methods=["PUT"])
def edit_question():
    data = request.json
    content_id = data.get("content_id")
    old_question = data.get("old_question")
    new_question_text = data.get("new_question")
    new_difficulty = data.get("new_difficulty")

    if not content_id or not old_question or not new_question_text or not new_difficulty:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    collection.update_one(
        {"content_id": content_id, "questions.question": old_question},
        {"$set": {"questions.$.question": new_question_text, "questions.$.difficulty": new_difficulty}}
    )

    return jsonify({"status": "success", "message": "Question updated successfully"})
