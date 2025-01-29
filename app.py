import os
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "service": "Smoker Q8 YouTube Notifier",
        "time": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "last_check": datetime.now().isoformat()
    }), 200

# Add this to handle both gunicorn and Flask's builtin server
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
