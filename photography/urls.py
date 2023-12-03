from django.urls import path
from .views import AddPhotography


urlpatterns = {
    path('', AddPhotography.as_view(), name='add_photography')
}