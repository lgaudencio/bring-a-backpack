from django.urls import path
from .views import AddDestination, Destinations, DestinationFullReview


urlpatterns = [
    path('', AddDestination.as_view(), name='add_destination'), 
    path('destinations/', Destinations.as_view(), name='destinations'),
    path('<slug:pk>/', DestinationFullReview.as_view(), name='destination_full_review'),
]