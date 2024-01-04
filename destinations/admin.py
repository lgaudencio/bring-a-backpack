from django.contrib import admin
from .models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """
    List for fields for destination review in admin panel
    """
    list_display = (
        'title',
        'brief',
        'photo',
        'review'
    )
