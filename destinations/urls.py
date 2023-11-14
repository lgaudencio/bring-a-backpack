from django.urls import path
from .views import AddDestination, Destinations


urlpatterns = [
    path('', AddDestination.as_view(), name='add_destination'), 
]