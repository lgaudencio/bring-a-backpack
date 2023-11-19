from django.urls import path
from .views import AddDestination, Destinations, DestinationFullReview, DeleteDestination, EditDestination


urlpatterns = [
    path('', AddDestination.as_view(), name='add_destination'), 
    path('destinations/', Destinations.as_view(), name='destinations'),
    path('<slug:pk>/', DestinationFullReview.as_view(), name='destination_full_review'),
    path('delete/<slug:pk>/', DeleteDestination.as_view(), name='destination_delete'),
    path('edit/<slug:pk>/', EditDestination.as_view(), name='edit_destination'), 
]