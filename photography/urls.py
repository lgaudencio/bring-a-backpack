from django.urls import path
from .views import AddPhotography, PhotographyList, PhotographyDetail


urlpatterns = [
    path('', AddPhotography.as_view(), name='add_photography'),
    path('photography_list/', PhotographyList.as_view(), name='photography_list'),
    path('<slug:pk>/', PhotographyDetail.as_view(), name='photography_full_post'), 
]