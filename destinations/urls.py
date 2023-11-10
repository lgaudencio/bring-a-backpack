from django.urls import path
from .views import AddDestination 


urlpatterns = [
    path('', AddDestination.as_view(), name='add_destination'), 
]