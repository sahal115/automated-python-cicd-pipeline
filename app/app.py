
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Python CI/CD Demo",
        "message": "Welcome to our automated deployment project!",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Python CI/CD Demo"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
