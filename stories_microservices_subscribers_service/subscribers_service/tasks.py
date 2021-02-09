from threading import Event
from .publisher import Publish
from .config.celery import celery
from .cache import ReadCache
from flask import render_template
from .models import SubscribersMail


@celery.task(name='send_mail_to_subscribers', task_time_limit=60, task_soft_time_limit=50,
             acks_late=True, autoretry_for=(Exception,), retry_backoff=True,
             retry_jitter=False, retry_kwargs={'max_retries': 3}, retry_backoff_max=60)

def send_mail_to_subscribers():
    cache = ReadCache()
    post_list = cache.load_data()
    to = []
    email_list = SubscribersMail.query.all()
    for i in email_list:
        to.append(i.email)
    if not post_list or not to:
        return False
    body = render_template('email_subscribers.html', post_list=post_list)
    subject = 'New posts from Stories'
    subtype = 'html'
    data = {
        'subject':subject,
        'body':body,
        'to': to,
        'subtype':subtype,
    }
    event_type = 'send_mail'
    Publish(data=data, event_type=event_type)
    return True