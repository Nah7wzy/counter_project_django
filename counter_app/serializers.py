from rest_framework import serializers
from .models import CounterHistory

class CounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterHistory
        fields = '__all__'
