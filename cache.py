import redis
import json

# Conecta no Redis
cache = redis.Redis(host="localhost", port=6379, db=0)

def get_cache(key: str):
    value = cache.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value: dict):
    cache.setex(key, 3600, json.dumps(value))  # 1 hora de cache
