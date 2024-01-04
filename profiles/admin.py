from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    List for fields for the profile in admin panel
    """
    list_display = (
        'pk',
        'user',
        'display_picture',
        'nationality',
        'traveler_type',
        'bio'
    )


admin.site.register(Profile, ProfileAdmin)
