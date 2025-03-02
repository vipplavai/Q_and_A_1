from flask import Flask, render_template
from routes.content_routes import content_routes
from routes.question_routes import question_routes

app = Flask(__name__)

# Register Routes
app.register_blueprint(content_routes)
app.register_blueprint(question_routes)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
