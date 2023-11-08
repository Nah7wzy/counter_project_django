from django.http import JsonResponse
from counter_app.serializers import CounterHistorySerializer
from counter_app.tasks import add_to_counter
from .models import CounterHistory
from rest_framework import status

# a view for the counter api
# add the provided value to the counter and queue a celery task to process it
def increment_counter(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        add_to_counter.delay(int(amount))
        return JsonResponse({'message': 'Task queued for processing.'})
    
#viw to fetch and display counter history
def get_counter_history(request):
    history = CounterHistory.objects.all()
    serializer = CounterHistorySerializer(history, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)