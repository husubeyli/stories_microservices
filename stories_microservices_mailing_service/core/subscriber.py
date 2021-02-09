from core.mail import SendMAil
from core.config import RedisConfig
import redis
import json




class Handler:

    def __init__(self, message):
        if message.get('type') == 'message':
            self.data = self.serialize_data(message)
            if self.find_event_type(self.data):
                mail_data = self.get_mail_data()
                self.send_mail(mail_data)
                

    def find_event_type(self, message):
        event_type = self.data.get('event_type')
       
        if event_type and event_type == 'send_mail':
            print(event_type)
            return True  
        print(event_type, 'event_type')
        return False 


    def serialize_data(self, message):
        data = message.get('data')
        return json.loads(data)

    def get_mail_data(self):
        return self.data.get('data')

    def send_mail(self, mail_data):
        print(mail_data)
        SendMAil(**mail_data)

def subscribe():
    redis_conn = RedisConfig.client()
    p = redis_conn.pubsub()
    p.subscribe(**{RedisConfig.CHANNEL_NAME: Handler})
    thread = p.run_in_thread()