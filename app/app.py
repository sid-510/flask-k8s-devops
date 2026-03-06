from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Siddhesh's Flask API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "flask-k8s-app",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "local")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)