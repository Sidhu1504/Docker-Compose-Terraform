from flask import Flask
from redis import Redis

app = Flask(__name__)
# connect to the redis service by name (compose service name = redis)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # redis.incr returns an integer
    count = redis.incr('hits')
    return f"This webpage has been viewed {count} time(s)\n"

if __name__ == "__main__":
    # debug True for dev only
    app.run(host="0.0.0.0", port=8000, debug=True)

