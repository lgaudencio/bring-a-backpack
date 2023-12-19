from django.contrib import admin
from .models import Photography


@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    """ 
    List for fields for photography post in admin panel
    """
    list_display = (
        'post_title', 
        'post_brief', 
        'main_photo',
        'photo_1',
        'photo_2',
        'photo_3',
        'photo_4',
        'photo_5',
        'photo_6',
        'photo_7',
        'photo_8',
        'photo_9'
    )
