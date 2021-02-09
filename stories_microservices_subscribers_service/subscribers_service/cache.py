import json
from .config.base import RedisConfig

class ReadCache(RedisConfig):

    def __init__(self):
        self.data_list = self.read()


    def load_data(self):
        return [json.loads(json.loads(data)) for data in self.data_list]


    def read(self):
        self.client = ReadCache.client()
        return self.client.lrange('posts', 0, -1)
    

    def delete(self):
        self.client.delete('posts')
