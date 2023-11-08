from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# do a standard celery configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'counter_project.settings')

app = Celery('counter_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# record the counter value every 10 minutes with a celery beat schedule
app.conf.beat_schedule = {
    'record-counter-value': {
        'task': 'counter_app.tasks.record_counter_value',
        'schedule': crontab(minute='*/10'),
    },
}

