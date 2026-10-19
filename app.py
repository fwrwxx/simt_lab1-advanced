from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "db"), port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("visits")
    return f"Hello from app! Visit count: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
