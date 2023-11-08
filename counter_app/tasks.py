from celery import shared_task #this decorator allows us to write a plain python function
from .models import Counter, CounterHistory
from datetime import datetime

# a celery task that increments the current value by the given amount
@shared_task
def add_to_counter(amount):
    counter = Counter.objects.first() # retrieve the first record from the database
    counter.value += amount
    counter.save()

# another task to record the counter value
@shared_task
def record_counter_value():
    counter = Counter.objects.first()
    timestamp = datetime.now()
    CounterHistory.objects.create(value=counter.value, timestamp=timestamp)
