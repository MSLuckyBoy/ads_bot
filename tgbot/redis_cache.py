from django.core.cache import cache
import json

class RedisCache:
    def __init__(self, prefix="cache_", timeout=None) -> None:
        self._prefix = prefix
        self._timeout = timeout

    def set(self, key, **kwargs):
        key = self._prefix + str(key)
        cache.set(key, json.dumps(kwargs), self._timeout)
    
    def get(self, key):
        key = self._prefix + str(key)

        if cache.get(key) is None:
            return None
        
        json_data = cache.get(key)
        data = json.loads(json_data)

        return data

    def delete(self, key):
        key = self._prefix + str(key)

        cache.delete(key)
