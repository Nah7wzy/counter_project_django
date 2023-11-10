from django.http import JsonResponse
from counter_app.serializers import CounterHistorySerializer
from counter_app.tasks import add_to_counter
from .models import CounterHistory
from rest_framework import status
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

# a view for the counter api
# add the provided value to the counter and queue a celery task to process it
@api_view(('POST',))
def increment_counter(request):
    if request.method == 'POST':
        request = json.loads(request.body)
        amount = request['amount']
        add_to_counter.delay(int(amount))
        return Response({'message': 'Task queued for processing.'})
    
#viw to fetch and display counter history
@api_view(('GET',))
def get_counter_history(request):
    history = CounterHistory.objects.all()
    serializer = CounterHistorySerializer(history, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)