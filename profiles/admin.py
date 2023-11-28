from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 
        'user',
        'display_picture',
        'nationality',
        'traveler type', 
        'bio'
    )

admin.site.register(Profile, ProfileAdmin)
