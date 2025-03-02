from flask import Blueprint, jsonify
from models.db import collection

content_routes = Blueprint("content_routes", __name__)

# Fetch Content & Questions by Content ID
@content_routes.route("/content/<content_id>", methods=["GET"])
def get_content(content_id):
    content_data = collection.find_one({"content_id": content_id})

    if content_data:
        return jsonify({
            "status": "success",
            "content": content_data["content"],
            "questions": content_data.get("questions", [])
        })
    else:
        return jsonify({"status": "error", "message": "Content ID not found"}), 404
