from django.db import models

# Model for the current counter value
class Counter(models.Model):
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

# Model for recording snapshots of the counter
class CounterHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} at {self.timestamp}"
