import json

from .config.base import RedisConfig

class SaveCache(RedisConfig):

    def __init__(self, obj):
        data = self.dump_data(obj)
        self.save(data)
        
    def dump_data(self, obj):
        return json.dumps(obj.to_dict())

    def save(self, data):
        print('data', data)
        client = SaveCache.client()
        client.rpush('posts', data)
