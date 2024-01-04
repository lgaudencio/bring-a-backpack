from django.urls import path
from .views import (
    AddPhotography, PhotographyList, PhotographyDetail, DeletePhotography,
    EditPhotography
)


urlpatterns = [
    path('', AddPhotography.as_view(), name='add_photography'),
    path(
        'photography_list/', PhotographyList.as_view(), name='photography_list'
    ),
    path(
        '<slug:pk>/', PhotographyDetail.as_view(), name='photography_full_post'
    ),
    path(
        'delete/<slug:pk>/', DeletePhotography.as_view(),
        name='delete_photography'
    ),
    path(
        'edit/<slug:pk>/', EditPhotography.as_view(), name='edit_photography'
    ),
]
