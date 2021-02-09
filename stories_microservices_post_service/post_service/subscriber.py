import redis
import json
from .config.base import RedisConfig
from .models import User


class Handler:

    def __init__(self, message):
        print('gordun isddemir print ele')
        if message.get("type") == "message":
            print(message, 'mesaj')
            self.data = self.serialize_data(message)
            if self.find_event_type():
                print('event type tapildi')
                user_data = self.get_user_data()
                self.save_user(user_data)
                

    def find_event_type(self):
        event_type = self.data.get('event_type')
        if event_type and event_type == 'user_created':
            return True
        return False

    def serialize_data(self, message):
        data = message.get('data')
        return json.loads(data)

    def get_user_data(self):
        return self.data.get('data')

    def save_user(self, data):
        user = User(**data)
        user.save()


def subscribe():
    redis_conn = RedisConfig.client()
    p = redis_conn.pubsub()
    p.subscribe(**{RedisConfig.CHANNEL_NAME: Handler})
    thread = p.run_in_thread()