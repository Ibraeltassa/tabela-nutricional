import redis
import json

redis_client = redis.Redis(host="tb-nutricional-cache", port=6379, db=0)

def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value, expire_seconds: int = 600):
    redis_client.set(key, json.dumps(value), ex=expire_seconds)
