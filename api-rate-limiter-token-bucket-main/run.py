from flask import Flask, jsonify, request
from app.limiter import TokenBucket

bucket = TokenBucket(rate=1, capacity=5)  # 1 request per second, burst up to 5

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    if bucket.allow_request():
        return jsonify({"message": "Request allowed ✅"})
    else:
        return jsonify({"error": "Too Many Requests ❌"}), 429
