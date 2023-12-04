from django.urls import path
from .views import AddPhotography, PhotographyList


urlpatterns = [
    path('', AddPhotography.as_view(), name='add_photography'),
    path('photography_list/', PhotographyList.as_view(), name='photography_list')
]