from flask import Flask, request, jsonify
import redis
import json
import os

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    return {"message": "Order API running"}

@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    r.lpush("orders", json.dumps(data))
    return {"status": "order queued"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
