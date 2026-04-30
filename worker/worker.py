import redis
import json
import time
import os

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

print("Worker started...")

while True:
    _, data = r.brpop("orders")
    order = json.loads(data)

    print(f"Processing order: {order}", flush=True)

    time.sleep(5) # simulate work

    print("Order completed", flush=True)
