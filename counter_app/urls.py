from django.urls import path
from . import views

# define a route
urlpatterns = [
    path('counter_history/', views.get_counter_history, name='counter_history'),
]
